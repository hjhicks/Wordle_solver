# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main-window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSlider, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(567, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.le_5 = QLineEdit(self.centralwidget)
        self.le_5.setObjectName(u"le_5")
        self.le_5.setEnabled(False)

        self.gridLayout.addWidget(self.le_5, 1, 4, 1, 1)

        self.s_3 = QSlider(self.centralwidget)
        self.s_3.setObjectName(u"s_3")
        self.s_3.setMaximum(26)
        self.s_3.setOrientation(Qt.Orientation.Vertical)

        self.gridLayout.addWidget(self.s_3, 2, 2, 1, 1)

        self.le_3 = QLineEdit(self.centralwidget)
        self.le_3.setObjectName(u"le_3")
        self.le_3.setEnabled(False)

        self.gridLayout.addWidget(self.le_3, 1, 2, 1, 1)

        self.le_4 = QLineEdit(self.centralwidget)
        self.le_4.setObjectName(u"le_4")
        self.le_4.setEnabled(False)

        self.gridLayout.addWidget(self.le_4, 1, 3, 1, 1)

        self.s_5 = QSlider(self.centralwidget)
        self.s_5.setObjectName(u"s_5")
        self.s_5.setMaximum(26)
        self.s_5.setOrientation(Qt.Orientation.Vertical)

        self.gridLayout.addWidget(self.s_5, 2, 4, 1, 1)

        self.s_4 = QSlider(self.centralwidget)
        self.s_4.setObjectName(u"s_4")
        self.s_4.setMaximum(26)
        self.s_4.setOrientation(Qt.Orientation.Vertical)

        self.gridLayout.addWidget(self.s_4, 2, 3, 1, 1)

        self.s_2 = QSlider(self.centralwidget)
        self.s_2.setObjectName(u"s_2")
        self.s_2.setMaximum(26)
        self.s_2.setOrientation(Qt.Orientation.Vertical)

        self.gridLayout.addWidget(self.s_2, 2, 1, 1, 1)

        self.le_2 = QLineEdit(self.centralwidget)
        self.le_2.setObjectName(u"le_2")
        self.le_2.setEnabled(False)

        self.gridLayout.addWidget(self.le_2, 1, 1, 1, 1)

        self.s_1 = QSlider(self.centralwidget)
        self.s_1.setObjectName(u"s_1")
        self.s_1.setMaximum(26)
        self.s_1.setOrientation(Qt.Orientation.Vertical)

        self.gridLayout.addWidget(self.s_1, 2, 0, 1, 1)

        self.le_1 = QLineEdit(self.centralwidget)
        self.le_1.setObjectName(u"le_1")
        self.le_1.setEnabled(False)

        self.gridLayout.addWidget(self.le_1, 1, 0, 1, 1)

        self.cb_1 = QCheckBox(self.centralwidget)
        self.cb_1.setObjectName(u"cb_1")

        self.gridLayout.addWidget(self.cb_1, 0, 0, 1, 1)

        self.cb_2 = QCheckBox(self.centralwidget)
        self.cb_2.setObjectName(u"cb_2")

        self.gridLayout.addWidget(self.cb_2, 0, 1, 1, 1)

        self.cb_3 = QCheckBox(self.centralwidget)
        self.cb_3.setObjectName(u"cb_3")

        self.gridLayout.addWidget(self.cb_3, 0, 2, 1, 1)

        self.cb_4 = QCheckBox(self.centralwidget)
        self.cb_4.setObjectName(u"cb_4")

        self.gridLayout.addWidget(self.cb_4, 0, 3, 1, 1)

        self.cb_5 = QCheckBox(self.centralwidget)
        self.cb_5.setObjectName(u"cb_5")

        self.gridLayout.addWidget(self.cb_5, 0, 4, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.whiteLettersLayout = QHBoxLayout()
        self.whiteLettersLayout.setObjectName(u"whiteLettersLayout")
        self.white_letters_label = QLabel(self.centralwidget)
        self.white_letters_label.setObjectName(u"white_letters_label")

        self.whiteLettersLayout.addWidget(self.white_letters_label)

        self.white_letters_input = QLineEdit(self.centralwidget)
        self.white_letters_input.setObjectName(u"white_letters_input")

        self.whiteLettersLayout.addWidget(self.white_letters_input)


        self.verticalLayout.addLayout(self.whiteLettersLayout)

        self.execute_btn = QPushButton(self.centralwidget)
        self.execute_btn.setObjectName(u"execute_btn")

        self.verticalLayout.addWidget(self.execute_btn)

        self.random_btn = QPushButton(self.centralwidget)
        self.random_btn.setObjectName(u"random_btn")

        self.verticalLayout.addWidget(self.random_btn)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 567, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.cb_1.setText(QCoreApplication.translate("MainWindow", u"Known Location", None))
        self.cb_2.setText(QCoreApplication.translate("MainWindow", u"Known Location", None))
        self.cb_3.setText(QCoreApplication.translate("MainWindow", u"Known Location", None))
        self.cb_4.setText(QCoreApplication.translate("MainWindow", u"Known Location", None))
        self.cb_5.setText(QCoreApplication.translate("MainWindow", u"Known Location", None))
        self.white_letters_label.setText(QCoreApplication.translate("MainWindow", u"White letters:", None))
        self.execute_btn.setText(QCoreApplication.translate("MainWindow", u"Find words", None))
        self.random_btn.setText(QCoreApplication.translate("MainWindow", u"View Possible Word", None))
    # retranslateUi

