

from PySide6.QtWidgets import QMainWindow, QDialog, QLabel, QVBoxLayout, QApplication
from uis.main_window import Ui_MainWindow
import random
from PySide6.QtCore import Qt

class WordleWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.possible_words = []
        self.ui.setupUi(self)
        for name in dir(self.ui):
            if not name.startswith('__') and hasattr(getattr(self.ui, name), 'objectName'):
                setattr(self, name, getattr(self.ui, name))

        self._link_slider_to_lineedit(self.s_1, self.le_1)
        self._link_slider_to_lineedit(self.s_2, self.le_2)
        self._link_slider_to_lineedit(self.s_3, self.le_3)
        self._link_slider_to_lineedit(self.s_4, self.le_4)
        self._link_slider_to_lineedit(self.s_5, self.le_5)

        self.execute_btn.clicked.connect(self.print_wordle_inputs)
        self.random_btn.clicked.connect(self.view_random_word)

    def print_wordle_inputs(self):
        lineedits = [self.le_1, self.le_2, self.le_3, self.le_4, self.le_5]
        checkboxes = [self.cb_1, self.cb_2, self.cb_3, self.cb_4, self.cb_5]
        letters = []
        for le in lineedits:
            text = le.text().strip().lower()
            if text == "n/a" or not text:
                letters.append('_')
            else:
                letters.append(text)
        known = ''.join([l if cb.isChecked() and l != '_' else '_' for l, cb in zip(letters, checkboxes)])
        has = ''.join(sorted(set([l for l in letters if l != '_' and l != 'n/a'])))
        allowed = ''.join(sorted(set([l for l in letters if l != 'n/a'])))
        allowed = ''.join(k for k in known if k != "_").join(self.white_letters_input.text().strip().lower())
        print(known, has, allowed)

        try:
            from uis.wordle_bridge import run_wordle_solver
            output = run_wordle_solver(known, has, allowed)
            self.possible_words = [w for w in output.split('\n') if w.strip()]
            print("Possible words:", self.possible_words)
        except Exception as e:
            print(f"Error running solver: {e}")

    def _link_slider_to_lineedit(self, slider, lineedit):
        def update_lineedit(value):
            if value == 0:
                lineedit.setText("N/A")
            else:
                lineedit.setText(chr(ord('A') + value - 1))
        slider.valueChanged.connect(update_lineedit)
        update_lineedit(slider.value())

    def view_random_word(self):
        if self.possible_words:
            # Move main window to a random location on the screen
            app = QApplication.instance()
            screen = app.primaryScreen()
            screen_geometry = screen.availableGeometry()
            win_w = self.width()
            win_h = self.height()
            max_x = max(0, screen_geometry.width() - win_w)
            max_y = max(0, screen_geometry.height() - win_h)
            rand_x = random.randint(screen_geometry.x(), screen_geometry.x() + max_x)
            rand_y = random.randint(screen_geometry.y(), screen_geometry.y() + max_y)
            self.move(rand_x, rand_y)

            word = random.choice(self.possible_words)
            print(f"Random possible word: {word}")
            dialog = QDialog(self)
            dialog.setWindowTitle("Random Word")
            layout = QVBoxLayout()
            label = QLabel(word)
            label.setAlignment(Qt.AlignCenter)
            layout.addWidget(label)
            dialog.setLayout(layout)
            # Show dialog as non-modal, under all windows
            dialog.setModal(False)
            dialog.setWindowModality(Qt.NonModal)
            if hasattr(Qt, 'WindowStaysOnBottomHint'):
                dialog.setWindowFlag(Qt.WindowStaysOnBottomHint, True)
            dialog.show()
            dialog.setFixedSize(200, 100)
        else:
            print("No possible words available. Please run the solver first.")
