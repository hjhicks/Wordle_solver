from PySide6.QtWidgets import QApplication, QMainWindow
from uis.wordle_widget import WordleWidget
import sys

def main():
    app = QApplication(sys.argv)
    window = WordleWidget()
    window.setWindowTitle("Wordle Solver")
    window.resize(600, 600)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
