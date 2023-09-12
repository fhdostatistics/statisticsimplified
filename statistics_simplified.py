import base64
import re
import sys
from io import BytesIO
from statistics import variance, stdev
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageQt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QSize
from PyQt5.QtWidgets import QApplication, QFormLayout, QGridLayout, QErrorMessage, QCheckBox, QLineEdit, QStyle, \
    QHBoxLayout, QSizePolicy, QWidget, QPushButton, QMessageBox, QVBoxLayout, QLabel, QMainWindow, QDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from pic2str import Formelsammlung, logo, Lizenz

class HilfeFenster(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1265, 708)
        self.imageScrollArea = QtWidgets.QScrollArea(self)
        self.imageScrollArea.setGeometry(QtCore.QRect(30, 30, 1220, 550))
        self.imageScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.imageScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.imageScrollArea.setWidgetResizable(True)
        self.imageScrollArea.setObjectName("imageScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 212, 152))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.imageLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.imageLabel.setGeometry(QtCore.QRect(0, 0, 285, 171))
        self.imageLabel.setAutoFillBackground(False)
        self.imageLabel.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.imageLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.imageLabel.setText("")
        self.imageLabel.setTextFormat(QtCore.Qt.AutoText)
        self.imageLabel.setScaledContents(False)
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setObjectName("imageLabel")
        self.imageScrollArea.setWidget(self.scrollAreaWidgetContents)
        lay = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self.imageLabel)

        # Load byte data
        byte_data = base64.b64decode(Formelsammlung)
        image_data = BytesIO(byte_data)
        image = Image.open(image_data)

        # PIL to QPixmap
        qImage = ImageQt.ImageQt(image)
        pixMap = QtGui.QPixmap.fromImage(qImage)

        # path = "Formelsammlung.png"
        # path = r"C:\Users\John\PycharmProjects\pythonProject\Formelsammlung.png"
        # pixMap = QtGui.QPixmap(path)
        self.imageLabel.setPixmap(pixMap)
        self.imageScrollArea.setWidgetResizable(True)
        self.imageLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(30, 600, 1200, 32))
        self.pushButton.setStyleSheet(
            "border: 1px; border-radius: 6px;background-color: #31708E; color:#ffffff; font:bold;;font-size: 20px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.close)
        self.pushButton.setText("Close")

class HinweiseFenster(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1265, 708)
        self.imageScrollArea = QtWidgets.QScrollArea(self)
        self.imageScrollArea.setGeometry(QtCore.QRect(30, 30, 1220, 550))
        self.imageScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.imageScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.imageScrollArea.setWidgetResizable(True)
        self.imageScrollArea.setObjectName("imageScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 212, 152))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.imageLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.imageLabel.setGeometry(QtCore.QRect(0, 0, 285, 171))
        self.imageLabel.setAutoFillBackground(False)
        self.imageLabel.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.imageLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.imageLabel.setText("")
        self.imageLabel.setTextFormat(QtCore.Qt.AutoText)
        self.imageLabel.setScaledContents(False)
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setObjectName("imageLabel")
        self.imageScrollArea.setWidget(self.scrollAreaWidgetContents)
        lay = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self.imageLabel)

        # Load byte data
        byte_data = base64.b64decode(Lizenz)
        image_data = BytesIO(byte_data)
        image = Image.open(image_data)

        # PIL to QPixmap
        qImage = ImageQt.ImageQt(image)
        pixMap = QtGui.QPixmap.fromImage(qImage)

        # path = "Formelsammlung.png"
        # path = r"C:\Users\John\PycharmProjects\pythonProject\Formelsammlung.png"
        # pixMap = QtGui.QPixmap(path)
        self.imageLabel.setPixmap(pixMap)
        self.imageScrollArea.setWidgetResizable(True)
        self.imageLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(30, 600, 1200, 32))
        self.pushButton.setStyleSheet(
            "border: 1px; border-radius: 6px;background-color: #31708E; color:#ffffff; font:bold;;font-size: 20px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.close)
        self.pushButton.setText("Close")

class TaschenrechnerFenster(QWidget):

    def __init__(self):
        super().__init__()
        self.setObjectName("Taschenrechner")
        self.setFixedSize(371, 568)
        self.setStyleSheet("background-color: #F7F9FB;")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(30, 20, 250, 40))
        self.outputLabel = QtWidgets.QLabel(self)
        self.outputLabel.setGeometry(QtCore.QRect(10, 10, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.outputLabel.setFont(font)
        self.outputLabel.setStyleSheet("font-size: 48px;")
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.outputLabel.setLineWidth(3)
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.cButton = QtWidgets.QPushButton(self, clicked=lambda: self.press_it("clear"))
        self.cButton.setGeometry(QtCore.QRect(10, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.cButton.setFont(font)
        self.cButton.setObjectName("cButton")
        self.cButton.setStyleSheet(
            '''
            *{
                border: 1px solid 'black';
                background-color: #88c0e6;
                border-radius: 6px;
                color: '#ffffff';
            }
            *:pressed{
                background: '#BC006C';
            }
            '''
        )
        self.openBButton = QtWidgets.QPushButton(self, clicked=lambda: self.press_it("("))
        self.openBButton.setGeometry(QtCore.QRect(100, 110, 75, 75))
        self.openBButton.setFont(font)
        self.openBButton.setObjectName("openBButton")
        self.openBButton.setStyleSheet(
            '''
            *{
                border: 1px solid 'black';
                background-color: #88c0e6;
                border-radius: 6px;
                color: '#ffffff';
            }
            *:pressed{
                background: '#BC006C';
            }
            '''
        )
        self.divisionButton = QtWidgets.QPushButton(self, clicked=lambda: self.press_it("/"))
        self.divisionButton.setGeometry(QtCore.QRect(275, 110, 75, 75))
        self.divisionButton.setFont(font)
        self.divisionButton.setObjectName("divisionButton")
        self.divisionButton.setStyleSheet(
            '''
            *{
                border: 1px solid 'black';
                background-color: #88c0e6;
                border-radius: 6px;
                color: '#ffffff';
            }
            *:pressed{
                background: '#BC006C';
            }
            '''
        )
        self.closeBButton = QtWidgets.QPushButton(self, clicked=lambda: self.press_it(")"))
        self.closeBButton.setGeometry(QtCore.QRect(190, 110, 75, 75))
        self.closeBButton.setFont(font)
        self.closeBButton.setObjectName("closeBButton")
        self.closeBButton.setStyleSheet(
            '''
            *{
                border: 1px solid 'black';
                background-color: #88c0e6;
                border-radius: 6px;
                color: '#ffffff';
            }
            *:pressed{
                background: '#BC006C';
            }
            '''
        )
        self.nineButton = QtWidgets.QPushButton(self, clicked=lambda: self.press_it("9"))
        self.nineButton.setGeometry(QtCore.QRect(190, 190, 75, 75))
        self.nineButton.setFont(font)
        self.nineButton.setObjectName("nineButton")
        self.nineButton.setStyleSheet(
            '''
            *{
                border: 1px solid 'black';
                background-color: #88c0e6;
                border-radius: 6px;
                color: '#ffffff';
            }
            *:pressed{
                background: '#BC006C';
            }
            '''
        )
        self.eightButton = QtWidgets.QPushButton(self, clicked=lambda: self.press_it("8"))
        self.eightButton.setGeometry(QtCore.QRect(100, 190, 75, 75))
        self.eightButton.setFont(font)
        self.eightButton.setObjectName("eightButton")
        self.eightButton.setStyleSheet(
            '''
            *{
                border: 1px solid 'black';
                background-color: #88c0e6;
                border-radius: 6px;
                color: '#ffffff';
            }
            *:pressed{
                background: '#BC006C';
            }
            '''
        )
        self.sevenButton = QtWidgets.QPushButton(self, clicked=lambda: self.press_it("7"))
        self.sevenButton.setGeometry(QtCore.QRect(10, 190, 75, 75))
        self.sevenButton.setFont(font)
        self.sevenButton.setObjectName("sevenButton")
        self.sevenButton.setStyleSheet(
            '''
            *{
                border: 1px solid 'black';
                background-color: #88c0e6;
                border-radius: 6px;
                color: '#ffffff';
            }
            *:pressed{
                background: '#BC006C';
            }
            '''
        )
        self.multiButton = QtWidgets.QPushButton(self, clicked=lambda: self.press_it("*"))
        self.multiButton.setGeometry(QtCore.QRect(275, 190, 75, 75))
        self.multiButton.setFont(font)
        self.multiButton.setObjectName("multiButton")
        self.multiButton.setStyleSheet(
            '''
            *{
                border: 1px solid 'black';
                background-color: #88c0e6;
                border-radius: 6px;
                color: '#ffffff';
            }
            *:pressed{
                background: '#BC006C';
            }
            '''
        )
        self.fourButton = QtWidgets.QPushButton(self, clicked=lambda: self.press_it("4"))
        self.fourButton.setGeometry(QtCore.QRect(10, 270, 75, 75))
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")
        self.fourButton.setStyleSheet(
            '''
            *{
                border: 1px solid 'black';
                background-color: #88c0e6;
                border-radius: 6px;
                color: '#ffffff';
            }
            *:pressed{
                background: '#BC006C';
            }
            '''
        )
        self.minusButton = QtWidgets.QPushButton(self, clicked=lambda: self.press_it("-"))
        self.minusButton.setGeometry(QtCore.QRect(275, 270, 75, 75))
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")
        self.minusButton.setStyleSheet(
            '''
            *{
                border: 1px solid 'black';
                background-color: #88c0e6;
                border-radius: 6px;
                color: '#ffffff';
            }
            *:pressed{
                background: '#BC006C';
            }
            '''
        )
        self.sixButton = QtWidgets.QPushButton(self, clicked=lambda: self.press_it("6"))
        self.sixButton.setGeometry(QtCore.QRect(190, 270, 75, 75))
        self.sixButton.setFont(font)
        self.sixButton.setObjectName("sixButton")
        self.sixButton.setStyleSheet(
            '''
            *{
                border: 1px solid 'black';
                background-color: #88c0e6;
                border-radius: 6px;
                color: '#ffffff';
            }
            *:pressed{
                background: '#BC006C';
            }
            '''
        )
        self.fiveButton = QtWidgets.QPushButton(self, clicked=lambda: self.press_it("5"))
        self.fiveButton.setGeometry(QtCore.QRect(100, 270, 75, 75))
        self.fiveButton.setFont(font)
        self.fiveButton.setObjectName("fiveButton")
        self.fiveButton.setStyleSheet(
            '''
            *{
                border: 1px solid 'black';
                background-color: #88c0e6;
                border-radius: 6px;
                color: '#ffffff';
            }
            *:pressed{
                background: '#BC006C';
            }
            '''
        )
        self.twoButton = QtWidgets.QPushButton(self, clicked=lambda: self.press_it("2"))
        self.twoButton.setGeometry(QtCore.QRect(100, 350, 75, 75))
        self.twoButton.setFont(font)
        self.twoButton.setObjectName("twoButton")
        self.twoButton.setStyleSheet(
            '''
            *{
                border: 1px solid 'black';
                background-color: #88c0e6;
                border-radius: 6px;
                color: '#ffffff';
            }
            *:pressed{
                background: '#BC006C';
            }
            '''
        )
        self.oneButton = QtWidgets.QPushButton(self, clicked=lambda: self.press_it("1"))
        self.oneButton.setGeometry(QtCore.QRect(10, 350, 75, 75))
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")
        self.oneButton.setStyleSheet(
            '''
            *{
                border: 1px solid 'black';
                background-color: #88c0e6;
                border-radius: 6px;
                color: '#ffffff';
            }
            *:pressed{
                background: '#BC006C';
            }
            '''
        )
        self.plusButton = QtWidgets.QPushButton(self, clicked=lambda: self.press_it("+"))
        self.plusButton.setGeometry(QtCore.QRect(275, 350, 75, 75))
        self.plusButton.setFont(font)
        self.plusButton.setObjectName("plusButton")
        self.plusButton.setStyleSheet(
            '''
            *{
                border: 1px solid 'black';
                background-color: #88c0e6;
                border-radius: 6px;
                color: '#ffffff';
            }
            *:pressed{
                background: '#BC006C';
            }
            '''
        )
        self.threeButton = QtWidgets.QPushButton(self, clicked=lambda: self.press_it("3"))
        self.threeButton.setGeometry(QtCore.QRect(190, 350, 75, 75))
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")
        self.threeButton.setStyleSheet(
            '''
            *{
                border: 1px solid 'black';
                background-color: #88c0e6;
                border-radius: 6px;
                color: '#ffffff';
            }
            *:pressed{
                background: '#BC006C';
            }
            '''
        )
        self.equalsButton = QtWidgets.QPushButton(self, clicked=lambda: self.math_it())
        self.equalsButton.setGeometry(QtCore.QRect(275, 430, 75, 75))
        self.equalsButton.setFont(font)
        self.equalsButton.setObjectName("equalsButton")
        self.equalsButton.setStyleSheet(
            '''
            *{
                border: 1px solid 'black';
                background-color: #88c0e6;
                border-radius: 6px;
                color: '#ffffff';
            }
            *:pressed{
                background: '#BC006C';
            }
            '''
        )
        self.commaButton = QtWidgets.QPushButton(self, clicked=lambda: self.dot_it())
        self.commaButton.setGeometry(QtCore.QRect(190, 430, 75, 75))
        self.commaButton.setFont(font)
        self.commaButton.setObjectName("commaButton")
        self.commaButton.setStyleSheet(
            '''
            *{
                border: 1px solid 'black';
                background-color: #88c0e6;
                border-radius: 6px;
                color: '#ffffff';
            }
            *:pressed{
                background: '#BC006C';
            }
            '''
        )
        self.zeroButton = QtWidgets.QPushButton(self, clicked=lambda: self.press_it("0"))
        self.zeroButton.setGeometry(QtCore.QRect(10, 430, 161, 75))
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")
        self.zeroButton.setStyleSheet(
            '''
            *{
                border: 1px solid 'black';
                background-color: #88c0e6;
                border-radius: 6px;
                color: '#ffffff';
            }
            *:pressed{
                background: '#BC006C';
            }
            '''
        )
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.clicked.connect(self.close)
        self.pushButton.setGeometry(QtCore.QRect(10, 510, 340, 50))
        self.pushButton.setStyleSheet(
            "border: 1px; border-radius: 6px;background-color: #31708E; color:#ffffff; font:bold;")

        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("Taschenrechner", "Close"))
        self.setWindowTitle(_translate("Taschenrechner", "Calculator"))
        self.outputLabel.setText(_translate("Taschenrechner", "0"))
        self.cButton.setText(_translate("Taschenrechner", "c"))
        self.openBButton.setText(_translate("Taschenrechner", "("))
        self.divisionButton.setText(_translate("Taschenrechner", "/"))
        self.closeBButton.setText(_translate("Taschenrechner", ")"))
        self.nineButton.setText(_translate("Taschenrechner", "9"))
        self.eightButton.setText(_translate("Taschenrechner", "8"))
        self.sevenButton.setText(_translate("Taschenrechner", "7"))
        self.multiButton.setText(_translate("Taschenrechner", "x"))
        self.fourButton.setText(_translate("Taschenrechner", "4"))
        self.minusButton.setText(_translate("Taschenrechner", "-"))
        self.sixButton.setText(_translate("Taschenrechner", "6"))
        self.fiveButton.setText(_translate("Taschenrechner", "5"))
        self.twoButton.setText(_translate("Taschenrechner", "2"))
        self.oneButton.setText(_translate("Taschenrechner", "1"))
        self.plusButton.setText(_translate("Taschenrechner", "+"))
        self.threeButton.setText(_translate("Taschenrechner", "3"))
        self.equalsButton.setText(_translate("Taschenrechner", "="))
        self.commaButton.setText(_translate("Taschenrechner", "."))
        self.zeroButton.setText(_translate("Taschenrechner", "0"))

    def dot_it(self):
        screen = self.outputLabel.text()
        if screen[-1] == ".":
            pass
        else:
            self.outputLabel.setText(f'{screen}.')

    def remove_it(self):
        screen = self.outputLabel.text()
        screen = screnn[:-1]
        self.outputLabel.setText(screen)

    def math_it(self):
        screen = self.outputLabel.text()
        try:
            answer = round(eval(screen), 3)
            self.outputLabel.setText(str(answer))
        except:
            self.outputLabel.setText("ERROR")

    def press_it(self, pressed):
        if pressed == "clear":
            self.outputLabel.setText("0")
        else:
            if self.outputLabel.text() == "0":
                self.outputLabel.setText(" ")
            self.outputLabel.setText(f'{self.outputLabel.text()}{pressed}')


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "statistics simplified"
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 600
        self.w1 = HilfeFenster()
        self.w2 = TaschenrechnerFenster()
        self.w3 = HinweiseFenster()
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setFixedSize(1100, 730)
        self.setStyleSheet("background-color:#F7F9FB;")
        self.main_widget = QtWidgets.QWidget(self)
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)
        self.uw = QLineEdit(self)
        self.pushbutton_formelsammlung = QtWidgets.QPushButton()
        self.pushbutton_formelsammlung.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #687864; color:#ffffff; font:bold;font-size: 20px;")
        self.pushbutton_formelsammlung.setObjectName("pushbutton_formelsammlung")
        self.pushbutton_formelsammlung.setText("Help")
        self.pushbutton_formelsammlung.clicked.connect(self.formelsammlung_oeffnen)
        self.pushButton_taschenrechner = QtWidgets.QPushButton()
        self.pushButton_taschenrechner.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #687864; color:#ffffff; font:bold;font-size: 20px;")
        self.pushButton_taschenrechner.setObjectName("pushButton_taschenrechner")
        self.pushButton_taschenrechner.setText("Calculator")
        self.pushButton_taschenrechner.clicked.connect(self.taschenrechner_oeffnen)
        self.pushButton_impressum = QtWidgets.QPushButton()
        self.pushButton_impressum.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #687864; color:#ffffff; font:bold;font-size: 20px;")
        self.pushButton_impressum.setObjectName("pushButton_impressum")
        self.pushButton_impressum.setText("Notes on use")

        self.pushButton_impressum.clicked.connect(self.impressum_anzeigen)
        buttonWindowBoxplot = QPushButton('Boxplot (***)', self)
        buttonWindowBoxplot.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #31708E; color:#ffffff; font:bold;font-size: 20px;")
        buttonWindowBoxplot.clicked.connect(self.buttonWindowBoxplot_onClick)
        buttonWindowBoxplot.setFixedSize(250, 250)

        pushButton_thema2 = QtWidgets.QPushButton('Histogram (**)', self)
        pushButton_thema2.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #5085A5; color:#ffffff; font:bold;font-size: 20px;")
        pushButton_thema2.setObjectName("pushButton_thema2")
        pushButton_thema2.clicked.connect(self.buttonHistogramm1_onClick)
        pushButton_thema2.setFixedSize(250, 250)

        pushButton_thema3 = QtWidgets.QPushButton('Boxplot (**)', self)
        pushButton_thema3.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #88c0e6; color:#ffffff; font:bold;font-size: 20px;")
        pushButton_thema3.setObjectName("pushButton_thema3")
        pushButton_thema3.clicked.connect(self.buttonWindowBoxplot1_onClick)
        pushButton_thema3.setFixedSize(250, 250)

        pushButton_thema4 = QtWidgets.QPushButton(self)
        pushButton_thema4.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #88c0e6; color:#ffffff; font:bold;font-size: 20px;")
        pushButton_thema4.setObjectName("pushButton_thema4")
        pushButton_thema4.clicked.connect(self.buttonKennzahl_onClick)
        pushButton_thema4.setFixedSize(250, 250)

        pushButton_thema5 = QtWidgets.QPushButton()
        pushButton_thema5.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #5085A5; color:#ffffff; font:bold;font-size: 20px;")
        pushButton_thema5.setObjectName("pushButton_thema5")
        pushButton_thema5.clicked.connect(self.buttonHistogramm2_onClick)
        pushButton_thema5.setFixedSize(250, 250)

        self.label_logo = QtWidgets.QLabel()
        self.label_logo.setText("")
        # Load byte data
        byte_data = base64.b64decode(logo)
        image_data = BytesIO(byte_data)
        image = Image.open(image_data)

        # PIL to QPixmap
        qImage = ImageQt.ImageQt(image)
        image = QtGui.QPixmap.fromImage(qImage)
        # QPixmap to QLabel
        self.label_logo.setPixmap(image)
        # self.label_logo.setPixmap(QtGui.QPixmap("logo.png"))
        # self.label_logo.setPixmap(QtGui.QPixmap(r"C:\Users\John\PycharmProjects\pythonProject\logo.png"))
        self.label_logo.setObjectName("label_logo")
        self.label_logo.setFixedSize(250, 250)
        pushButton_thema4.setText("Measures (*)")
        pushButton_thema5.setText("Histogram (***)")

        h1 = QHBoxLayout()
        h1.addWidget(self.pushbutton_formelsammlung)
        h1.addWidget(self.pushButton_taschenrechner)
        h1.addWidget(self.pushButton_impressum)
        h3 = QHBoxLayout()
        h3.addWidget(pushButton_thema4)
        h3.addWidget(pushButton_thema2)
        h3.addWidget(pushButton_thema5)
        h4 = QHBoxLayout()
        h4.addWidget(pushButton_thema3)
        h4.addWidget(buttonWindowBoxplot)
        h4.addWidget(self.label_logo)
        layout = QVBoxLayout()
        layout.addLayout(h1)
        layout.addLayout(h3)
        layout.addLayout(h4)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()

    def closeEvent(self, event):
        if self.w1:
            self.w1.close()
        if self.w2:
            self.w2.close()
        if self.w3:
            self.w3.close()

    def buttonWindowBoxplot_onClick(self):
        self.cams = Boxplot2()
        self.cams.show()
        self.close()

    def buttonHistogramm1_onClick(self):
        self.cams = Histogramm1()
        self.cams.show()
        self.close()

    def buttonHistogramm2_onClick(self):
        self.cams = Histogramm2()
        self.cams.show()
        self.close()

    def buttonWindowBoxplot1_onClick(self):
        self.cams = Boxplot1()
        self.cams.show()
        self.close()

    def buttonKennzahl_onClick(self):
        self.cams = Kennzahlen()
        self.cams.show()
        self.close()

    def formelsammlung_oeffnen(self, checked):
        if self.w1.isVisible():
            self.w1.hide()

        else:
            self.w1.show()

    def impressum_anzeigen(self):
        if self.w3.isVisible():
            self.w3.hide()

        else:
            self.w3.show()

    def taschenrechner_oeffnen(self):
        if self.w2.isVisible():
            self.w2.hide()

        else:
            self.w2.show()

class Kennzahlen(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 800
        self.w1 = HilfeFenster()
        self.w2 = TaschenrechnerFenster()
        self.w3 = HinweiseFenster()
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setFixedSize(1100, 730)
        self.setWindowTitle('Key figures task generator')
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)


        self.pushbutton_formelsammlung = QtWidgets.QPushButton()
        self.pushbutton_formelsammlung.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #687864; color:#ffffff; font:bold;font-size: 20px;")
        self.pushbutton_formelsammlung.setObjectName("pushbutton_formelsammlung")
        self.pushbutton_formelsammlung.setText("Help")
        self.pushbutton_formelsammlung.clicked.connect(self.formelsammlung_oeffnen)
        self.pushButton_taschenrechner = QtWidgets.QPushButton()
        self.pushButton_taschenrechner.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #687864; color:#ffffff; font:bold;font-size: 20px;")
        self.pushButton_taschenrechner.setObjectName("pushButton_taschenrechner")
        self.pushButton_taschenrechner.setText("Calculator")
        self.pushButton_taschenrechner.clicked.connect(self.taschenrechner_oeffnen)
        self.pushButton_impressum = QtWidgets.QPushButton()
        self.pushButton_impressum.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #687864; color:#ffffff; font:bold;font-size: 20px;")
        self.pushButton_impressum.setObjectName("pushButton_impressum")
        self.pushButton_impressum.setText("Hints on use")
        self.pushButton_impressum.clicked.connect(self.hinweise_oeffnen)

        self.button = QPushButton('Solution')
        self.button2 = QPushButton('New task')
        self.button3 = QPushButton('Main page')
        self.button2.clicked.connect(self.newdata)
        self.button.clicked.connect(self.plot)
        self.button3.clicked.connect(self.goMainWindow)
        self.button2.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #31708E; color:#ffffff; font:bold;font-size: 20px;")
        self.button.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #31708E; color:#ffffff; font:bold;font-size: 20px;")
        self.button3.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #31708E; color:#ffffff; font:bold;font-size: 20px;")

        self.aufgabe = QLabel("aufgabe")

        self.daten = QLabel("daten")
        self.aufgabe.setStyleSheet("color:#31708E;""border-color: #31708E;font-size: 20px;")
        self.daten.setStyleSheet("color:#687864;""border-color: #31708E;font-size: 20px;")
        self.aufgabe.setText("Berechnen Sie die untenstehenden Kennzahlen für die folgenden Daten:")
        self.daten.setText("Click on new task")
        self.button = QPushButton('Solution')
        self.button2 = QPushButton('New task')
        self.button2.clicked.connect(self.newdata)
        self.button.clicked.connect(self.plot)
        self.button2.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #31708E; color:#ffffff; font:bold;font-size: 20px;")
        self.button.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #31708E; color:#ffffff; font:bold;font-size: 20px;")

        self.mean_label = QLabel("Arithmetic mean:")
        self.mean_label.setStyleSheet("color:#31708E;border-color: #31708E;font-size: 20px;")
        self.mean = QLineEdit(self)
        self.mean.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.mean.setText("")
        self.mean.setFixedSize(100, 25)

        self.median_label = QLabel("Median:")
        self.median_label.setStyleSheet("color:#31708E;border-color: #31708E;font-size: 20px;")
        self.median = QLineEdit(self)
        self.median.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.median.setText("")
        self.median.setFixedSize(100, 25)

        self.span_label = QLabel("Span:")
        self.span_label.setStyleSheet("color:#31708E;border-color: #31708E;font-size: 20px;")
        self.span = QLineEdit(self)
        self.span.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.span.setText("")
        self.span.setFixedSize(100, 25)

        self.var_label = QLabel("Sample variance:")
        self.var_label.setStyleSheet("color:#31708E;border-color: #31708E;font-size: 20px;")
        self.var = QLineEdit(self)
        self.var.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.var.setText("")
        self.var.setFixedSize(100, 25)

        self.std_label = QLabel("Standard deviation:")
        self.std_label.setStyleSheet("color:#31708E;border-color: #31708E;font-size: 20px;")
        self.std = QLineEdit(self)
        self.std.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.std.setText("")
        self.std.setFixedSize(100, 25)
        self.newdata()

        outerLayout = QVBoxLayout()
        mLayout = QHBoxLayout()
        mLayout.addWidget(self.pushbutton_formelsammlung)
        mLayout.addWidget(self.pushButton_taschenrechner)
        mLayout.addWidget(self.pushButton_impressum)
        middleLayout2 = QFormLayout()
        middleLayout2.addRow(self.mean_label, self.mean)
        middleLayout2.addRow(self.median_label, self.median)
        middleLayout2.addRow(self.span_label, self.span)
        middleLayout2.addRow(self.var_label, self.var)
        middleLayout2.addRow(self.std_label, self.std)
        middleLayout = QHBoxLayout()
        middleLayout.addLayout(middleLayout2)
        middleLayout.addStretch(4)
        bottomLayout = QHBoxLayout()
        bottomLayout.addWidget(self.button3)
        bottomLayout.addWidget(self.button2)
        bottomLayout.addWidget(self.button)
        outerLayout.addLayout(mLayout)
        outerLayout.addStretch(1)
        outerLayout.addWidget(self.aufgabe)
        outerLayout.addWidget(self.daten)
        outerLayout.addStretch(2)
        outerLayout.addLayout(middleLayout)
        outerLayout.addStretch(1)
        outerLayout.addLayout(bottomLayout)
        self.setLayout(outerLayout)

    def closeEvent(self, event):
        if self.w1:
            self.w1.close()
        if self.w2:
            self.w2.close()
        if self.w3:
            self.w3.close()

    def goMainWindow(self):
        self.cams = Window()
        self.cams.show()
        self.close()

    def get_quantile(self, data, p):
        data = np.sort(data)
        index = int(len(data) * p)
        test = len(data) * p
        if test.is_integer():
            q = (data[index - 1] + data[index]) / 2
        else:
            q = data[index]
        return q

    def newdata(self):

        rand_n = (np.random.randint(10, high=12, size=None, dtype=int))
        rand_mean = (np.random.randint(12, high=20, size=None, dtype=int))
        data = np.random.normal(rand_mean, rand_mean / 3, rand_n)
        data = data.astype(int)
        text = (
                "Calculate the metrics below for the following data (n= "+ str((len(data))) +") :")
        data2 = np.array2string(data, separator=',')
        data2 = (data2[1:-1])
        self.aufgabe.setText(text)
        self.daten.setText((str(data2)))
        self.aufgabe.setStyleSheet("color:#31708E;border-color: #31708E;font-size: 20px;")
        self.daten.setStyleSheet("color:#31708E;border-color: #31708E;font-size: 20px;")

        self.mean.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.median.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.var.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.std.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.span.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")

        self.mean.setText("")
        self.median.setText("")
        self.var.setText("")
        self.std.setText("")
        self.span.setText("")

    def plot(self):

        # check solution
        try:
            data = self.daten.text()
            data = re.findall(r'\d+', data)
            data = list(map(int, data))
        except:
            self.newdata()

        # check solution
        try:
            r = max(data) - min(data)
            if float(self.mean.text()) == round(np.mean(data), 3):
                self.mean.setStyleSheet("color:green;font-size: 20px;")
            else:
                self.mean.setStyleSheet("color:red;font-size: 20px;")
            if float(self.median.text()) == round(self.get_quantile(data,0.5), 3):
                self.median.setStyleSheet("color:green;font-size: 20px;")
            else:
                self.median.setStyleSheet("color:red;font-size: 20px;")
            if (round(variance(data), 3) - 0.002) <= float(self.var.text()) <= (round(variance(data), 3) + 0.002):
                self.var.setStyleSheet("color:green;font-size: 20px;")
            else:
                self.var.setStyleSheet("color:red;font-size: 20px;")
            if float(self.span.text()) == r:
                self.span.setStyleSheet("color:green;font-size: 20px;")
            else:
                self.span.setStyleSheet("color:red;font-size: 20px;")
            if  (round(stdev(data), 3)-0.002) <= float(self.std.text()) <= (round(stdev(data), 3)+0.002):
                self.std.setStyleSheet("color:green;font-size: 20px;")
            else:
                self.std.setStyleSheet("color:red;font-size: 20px;")
        except:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error!")
            dlg.setText(
                "Your answers cannot be evaluated. Enter a value for each field. Also pay attention to the format: 4.5. Round to 3 decimal places. Then you can check your answers again.")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Warning)
            button = dlg.exec()

    def formelsammlung_oeffnen(self, checked):
        if self.w1.isVisible():
            self.w1.hide()

        else:
            self.w1.show()

    def hinweise_oeffnen(self):
        if self.w3.isVisible():
            self.w3.hide()

        else:
            self.w3.show()

    def taschenrechner_oeffnen(self):
        if self.w2.isVisible():
            self.w2.hide()

        else:
            self.w2.show()

class Boxplot1(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 800
        self.w1 = HilfeFenster()
        self.w2 = TaschenrechnerFenster()
        self.w3 = HinweiseFenster()
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setFixedSize(1100, 730)
        self.setWindowTitle('Simple boxplot task generator')
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)


        self.pushbutton_formelsammlung = QtWidgets.QPushButton()
        self.pushbutton_formelsammlung.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #687864; color:#ffffff; font:bold;font-size: 20px;")
        self.pushbutton_formelsammlung.setObjectName("pushbutton_formelsammlung")
        self.pushbutton_formelsammlung.setText("Help")
        self.pushbutton_formelsammlung.clicked.connect(self.formelsammlung_oeffnen)
        self.pushButton_taschenrechner = QtWidgets.QPushButton()
        self.pushButton_taschenrechner.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #687864; color:#ffffff; font:bold;font-size: 20px;")
        self.pushButton_taschenrechner.setObjectName("pushButton_taschenrechner")
        self.pushButton_taschenrechner.setText("Calculator")
        self.pushButton_taschenrechner.clicked.connect(self.taschenrechner_oeffnen)
        self.pushButton_impressum = QtWidgets.QPushButton()
        self.pushButton_impressum.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #687864; color:#ffffff; font:bold;font-size: 20px;")
        self.pushButton_impressum.setObjectName("pushButton_impressum")
        self.pushButton_impressum.setText("Hints on use")
        self.pushButton_impressum.clicked.connect(self.hinweise_oeffnen)

        self.aufgabe = QLabel("aufgabe")
        self.daten = QLabel("daten")
        self.aufgabe.setStyleSheet("color:#31708E;border-color: #31708E;font-size: 20px;")
        self.daten.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        self.aufgabe.setText(("Create a simple boxplot for the following data:"))
        self.daten.setText("Click on new task")
        self.aufgabe.setStyleSheet("color:#31708E;border-color: #31708E;font-size: 20px;")
        self.daten.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")

        self.button = QPushButton('Solution')
        self.button2 = QPushButton('New task')
        self.button3 = QPushButton('Main page')
        self.button2.clicked.connect(self.newdata)
        self.button.clicked.connect(self.plot)
        self.button3.clicked.connect(self.goMainWindow)
        self.button2.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #31708E; color:#ffffff; font:bold;font-size: 20px;")
        self.button.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #31708E; color:#ffffff; font:bold;font-size: 20px;")
        self.button3.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #31708E; color:#ffffff; font:bold;font-size: 20px;")
        self.uw = QLineEdit(self)
        self.uw.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.uw.setPlaceholderText("lower whisker")

        self.uq = QLineEdit(self)
        self.uq.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.uq.setPlaceholderText("1st quartile")

        self.med = QLineEdit(self)
        self.med.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.med.setPlaceholderText("median")

        self.oq = QLineEdit(self)
        self.oq.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.oq.setPlaceholderText("3rd quartile")

        self.ow = QLineEdit(self)
        self.ow.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.ow.setPlaceholderText("upper whisker")

        mLayout = QHBoxLayout()
        mLayout.addWidget(self.pushbutton_formelsammlung)
        mLayout.addWidget(self.pushButton_taschenrechner)
        mLayout.addWidget(self.pushButton_impressum)
        topLayout = QHBoxLayout()
        topLayout.addWidget(self.aufgabe)
        topLayout.addWidget(self.daten)
        middleLayout = QHBoxLayout()
        middleLayout.addWidget(self.uw)
        middleLayout.addWidget(self.uq)
        middleLayout.addWidget(self.med)
        middleLayout.addWidget(self.oq)
        middleLayout.addWidget(self.ow)
        bottomLayout = QHBoxLayout()
        bottomLayout.addWidget(self.button3)
        bottomLayout.addWidget(self.button2)
        bottomLayout.addWidget(self.button)
        outerLayout = QVBoxLayout()
        outerLayout.addLayout(mLayout)
        outerLayout.addLayout(topLayout)
        outerLayout.addLayout(middleLayout)
        outerLayout.addWidget(self.canvas)
        outerLayout.addLayout(bottomLayout)
        self.setLayout(outerLayout)

    def closeEvent(self, event):
        if self.w1:
            self.w1.close()
        if self.w2:
            self.w2.close()
        if self.w3:
            self.w3.close()

    def goMainWindow(self):
        self.cams = Window()
        self.cams.show()
        self.close()

    def newdata(self):
        self.figure.clear()
        plt.draw()
        rand_n = (np.random.randint(10, high=13, size=None, dtype=int))
        rand_mean = (np.random.randint(8, high=20, size=None, dtype=int))

        data = np.random.normal(rand_mean, rand_mean / 4, rand_n)
        data = data.astype(int)
        data = abs(data)
        data = np.array2string(data, separator=',')
        data = (data[1:-1])
        self.daten.setText((str(data)))
        self.aufgabe.setText(("Create a simple boxplot for the data(n= " + str(rand_n)+"):"))
        self.aufgabe.setStyleSheet("color:#31708E;border-color: #31708E;font-size: 20px;")
        self.daten.setStyleSheet("color:#31708E;border-color: #31708E;font-size: 20px;")

        self.uw.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.uq.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.med.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.oq.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.ow.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")

        self.uw.setText("")
        self.uq.setText("")
        self.med.setText("")
        self.oq.setText("")
        self.ow.setText("")

        self.uw.setPlaceholderText("lower whisker")
        self.uq.setPlaceholderText("1st quartile")
        self.med.setPlaceholderText("median")
        self.oq.setPlaceholderText("3rd quartile")
        self.ow.setPlaceholderText("upper whisker")

    def get_quantile(self, data, p):
        data = np.sort(data)
        index = int(len(data) * p)
        test = len(data) * p
        if test.is_integer():
            q = (data[index - 1] + data[index]) / 2
        else:
            q = data[index]
        return q

    def plot(self):
        try:
            data = self.daten.text()
            data = re.findall(r'\d+', data)
            data = list(map(int, data))
            boxes = [
                {
                    'label': "",
                    'whislo': min(data),  # Bottom whisker position
                    'q1': self.get_quantile(data, 0.25),  # First quartile (25th percentile)
                    'med': self.get_quantile(data, 0.5),  # Median         (50th percentile)
                    'q3': self.get_quantile(data, 0.75),  # Third quartile (75th percentile)
                    'whishi': max(data),  # Top whisker position
                    'fliers': []  # Outliers
                }
            ]
            # clearing old figure
            self.figure.clear()

            # create an axis
            ax = self.figure.add_subplot(111)
            ax.set(xlabel="", ylabel="x")

            # plot data
            ax.bxp(boxes, showfliers=True)
            plt.xticks([])

            # refresh canvas
            self.canvas.draw()
            # check solution

        except:
            self.newdata()
        try:
            if float(self.uw.text()) == min(data):
                self.uw.setStyleSheet("color:green;font-size: 20px;")
            else:
                self.uw.setStyleSheet("color:red;font-size: 20px;")
            if float(self.uq.text()) == self.get_quantile(data, 0.25):
                self.uq.setStyleSheet("color:green;font-size: 20px;")
            else:
                self.uq.setStyleSheet("color:red;font-size: 20px;")
            if float(self.med.text()) == self.get_quantile(data, 0.5):  # np.median(data):
                self.med.setStyleSheet("color:green;font-size: 20px;")
            else:
                self.med.setStyleSheet("color:red;font-size: 20px;")
            if float(self.oq.text()) == self.get_quantile(data, 0.75):
                self.oq.setStyleSheet("color:green;font-size: 20px;")
            else:
                self.oq.setStyleSheet("color:red;font-size: 20px;")
            if float(self.ow.text()) == max(data):
                self.ow.setStyleSheet("color:green;font-size: 20px;")
            else:
                self.ow.setStyleSheet("color:red;font-size: 20px;")
        except:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error!")
            dlg.setText(
                "Your answers cannot be evaluated. Enter a value for each field. Also pay attention to the format: 4.5. Round to 3 decimal places. Then you can check your answers again.")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Warning)
            button = dlg.exec()

    def formelsammlung_oeffnen(self, checked):
        if self.w1.isVisible():
            self.w1.hide()

        else:
            self.w1.show()

    def hinweise_oeffnen(self):
        if self.w3.isVisible():
            self.w3.hide()

        else:
            self.w3.show()

    def taschenrechner_oeffnen(self):
        if self.w2.isVisible():
            self.w2.hide()

        else:
            self.w2.show()

class Boxplot2(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 800
        self.w1 = HilfeFenster()
        self.w2 = TaschenrechnerFenster()
        self.w3 = HinweiseFenster()
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setFixedSize(1100, 730)
        self.setWindowTitle('Refined boxplot task generator')
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)


        self.pushbutton_formelsammlung = QtWidgets.QPushButton()
        self.pushbutton_formelsammlung.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #687864; color:#ffffff; font:bold;font-size: 20px;")
        self.pushbutton_formelsammlung.setObjectName("pushbutton_formelsammlung")
        self.pushbutton_formelsammlung.setText("Help")
        self.pushbutton_formelsammlung.clicked.connect(self.formelsammlung_oeffnen)
        self.pushButton_taschenrechner = QtWidgets.QPushButton()
        self.pushButton_taschenrechner.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #687864; color:#ffffff; font:bold;font-size: 20px;")
        self.pushButton_taschenrechner.setObjectName("pushButton_taschenrechner")
        self.pushButton_taschenrechner.setText("Calculator")
        self.pushButton_taschenrechner.clicked.connect(self.taschenrechner_oeffnen)
        self.pushButton_impressum = QtWidgets.QPushButton()
        self.pushButton_impressum.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #687864; color:#ffffff; font:bold;font-size: 20px;")
        self.pushButton_impressum.setObjectName("pushButton_impressum")
        self.pushButton_impressum.setText("Hints on use")
        self.pushButton_impressum.clicked.connect(self.hinweise_oeffnen)

        self.aufgabe = QLabel("aufgabe")
        self.daten = QLabel("daten")
        self.aufgabe.setStyleSheet("color:#31708E;border-color: #31708E;font-size: 20px;")
        self.daten.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        self.aufgabe.setText(("Create a refined boxplot for the following data:"))
        self.daten.setText("Click on new task")
        self.aufgabe.setStyleSheet("color:#31708E;""border-color: #31708E;font-size: 20px;")
        self.daten.setStyleSheet("color:#687864;""border-color: #31708E;font-size: 20px;")

        self.button = QPushButton('Solution')
        self.button2 = QPushButton('New task')
        self.button3 = QPushButton('main page')
        self.button2.clicked.connect(self.newdata)
        self.button.clicked.connect(self.plot)
        self.button3.clicked.connect(self.goMainWindow)
        self.button2.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #31708E; color:#ffffff; font:bold;font-size: 20px;")
        self.button.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #31708E; color:#ffffff; font:bold;font-size: 20px;")
        self.button3.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #31708E; color:#ffffff; font:bold;font-size: 20px;")
        self.uw = QLineEdit(self)
        self.uw.setStyleSheet("color:#687864;""border-color: #31708E;font-size: 20px;")
        self.uw.setPlaceholderText("lower whisker")

        self.uq = QLineEdit(self)
        self.uq.setStyleSheet("color:#687864;""border-color: #31708E;font-size: 20px;")
        self.uq.setPlaceholderText("1st quartile")

        self.med = QLineEdit(self)
        self.med.setStyleSheet("color:#687864;""border-color: #31708E;font-size: 20px;")
        self.med.setPlaceholderText("median")

        self.oq = QLineEdit(self)
        self.oq.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.oq.setPlaceholderText("3rd quartile")

        self.ow = QLineEdit(self)
        self.ow.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.ow.setPlaceholderText("upper whisker")

        self.a = QCheckBox(self)
        self.a.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.a.setText("outlier")

        outerLayout = QVBoxLayout()
        mLayout = QHBoxLayout()
        mLayout.addWidget(self.pushbutton_formelsammlung)
        mLayout.addWidget(self.pushButton_taschenrechner)
        mLayout.addWidget(self.pushButton_impressum)
        topLayout = QHBoxLayout()
        topLayout.addWidget(self.aufgabe)
        topLayout.addWidget(self.daten)
        middleLayout = QHBoxLayout()
        middleLayout.addWidget(self.uw)
        middleLayout.addWidget(self.uq)
        middleLayout.addWidget(self.med)
        middleLayout.addWidget(self.oq)
        middleLayout.addWidget(self.ow)
        middleLayout.addWidget(self.a)
        bottomLayout = QHBoxLayout()
        bottomLayout.addWidget(self.button3)
        bottomLayout.addWidget(self.button2)
        bottomLayout.addWidget(self.button)
        outerLayout.addLayout(mLayout)
        outerLayout.addLayout(topLayout)
        outerLayout.addLayout(middleLayout)
        outerLayout.addWidget(self.canvas)
        outerLayout.addLayout(bottomLayout)
        self.setLayout(outerLayout)

    def closeEvent(self, event):
        if self.w1:
            self.w1.close()
        if self.w2:
            self.w2.close()
        if self.w3:
            self.w3.close()

    def goMainWindow(self):
        self.cams = Window()
        self.cams.show()
        self.close()

    def newdata(self):
        self.figure.clear()
        plt.draw()
        rand_n = (np.random.randint(9, high=12, size=None, dtype=int))
        rand_mean = (np.random.randint(10, high=25, size=None, dtype=int))
        data = np.random.normal(rand_mean, rand_mean / 4, rand_n)
        if rand_mean > 17:
            data = np.append(data, 1)
        else:
            data = np.append(data, rand_mean * 2)
        data = data.astype(int)
        data = abs(data)
        np.random.shuffle(data)
        self.aufgabe.setText("Create a refined boxplot for the data (n= "+ str(len(data)) +") :")
        data = np.array2string(data, separator=',')
        data = (data[1:-1])
        self.daten.setText((str(data)))
        self.aufgabe.setStyleSheet("color:#31708E;border-color: #31708E;font-size: 20px;")
        self.daten.setStyleSheet("color:#31708E;border-color: #31708E;font-size: 20px;")

        self.uw.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.uq.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.med.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.oq.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.ow.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.a.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")

        self.uw.setText("")
        self.uq.setText("")
        self.med.setText("")
        self.oq.setText("")
        self.ow.setText("")
        self.a.setChecked(False)

        self.uw.setPlaceholderText("lower whisker")
        self.uq.setPlaceholderText("1st quartile")
        self.med.setPlaceholderText("median")
        self.oq.setPlaceholderText("3rd quartile")
        self.ow.setPlaceholderText("upper whisker")
        self.a.setText("Outlier")

    def get_quantile(self, data, p):
        data = np.sort(data)
        index = int(len(data) * p)
        test = len(data) * p
        if test.is_integer():
            q = (data[index - 1] + data[index]) / 2
        else:
            q = data[index]
        return q

    # def plot(self, data):
    def plot(self):

        self.figure.clear()
        # check solution
        try:
            data = self.daten.text()
            data = re.findall(r'\d+', data)
            data = list(map(int, data))

            B = plt.boxplot(data)
            outliers = [flier.get_ydata() for flier in B["fliers"]]
            q1 = self.get_quantile(data, 0.25)
            q2 = self.get_quantile(data, 0.5)
            q3 = self.get_quantile(data, 0.75)
            whiskers = [whiskers.get_ydata() for whiskers in B["whiskers"]]
            if (outliers[0].size == 0):
                outliers = []
            boxes = [
                {
                    'label': "",
                    'whislo': whiskers[0][1],  # Bottom whisker position
                    'q1': q1,  # First quartile (25th percentile)
                    'med': q2,  # Median         (50th percentile)
                    'q3': q3,  # Third quartile (75th percentile)
                    'whishi': whiskers[1][1],  # Top whisker position
                    'fliers': outliers  # Outliers
                }
            ]
            # clearing old figure
            self.figure.clear()

            # create an axis
            ax = self.figure.add_subplot(111)
            ax.set(xlabel="", ylabel="x")

            # plot data
            ax.bxp(boxes, showfliers=True)
            plt.xticks([])

            # refresh canvas
            self.canvas.draw()
            # check solution
            outliers = [flier.get_ydata() for flier in B["fliers"]]
        except:
            self.newdata()
        try:
            if float(self.uw.text()) == whiskers[0][1]:
                self.uw.setStyleSheet("color:green;font-size: 20px;")
            else:
                self.uw.setStyleSheet("color:red;font-size: 20px;")
            if float(self.uq.text()) == q1:
                self.uq.setStyleSheet("color:green;font-size: 20px;")
            else:
                self.uq.setStyleSheet("color:red;font-size: 20px;")
            if float(self.med.text()) == q2:
                self.med.setStyleSheet("color:green;font-size: 20px;")
            else:
                self.med.setStyleSheet("color:red;font-size: 20px;")
            if float(self.oq.text()) == q3:
                self.oq.setStyleSheet("color:green;font-size: 20px;")
            else:
                self.oq.setStyleSheet("color:red;font-size: 20px;")
            if float(self.ow.text()) == whiskers[1][1]:
                self.ow.setStyleSheet("color:green;font-size: 20px;")
            else:
                self.ow.setStyleSheet("color:red;font-size: 20px;")
            if (self.a.isChecked()) == (outliers[0].size > 0):
                self.a.setStyleSheet("color:green;font-size: 20px;")
            else:
                self.a.setStyleSheet("color:red;font-size: 20px;")
        except:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error!")
            dlg.setText(
                "Your answers cannot be evaluated. Enter a value for each field. Also pay attention to the format: 4.5. Round to 3 decimal places. Then you can check your answers again.")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Warning)
            button = dlg.exec()

    def formelsammlung_oeffnen(self, checked):
        if self.w1.isVisible():
            self.w1.hide()

        else:
            self.w1.show()

    def hinweise_oeffnen(self):
        if self.w3.isVisible():
            self.w3.hide()

        else:
            self.w3.show()

    def taschenrechner_oeffnen(self):
        if self.w2.isVisible():
            self.w2.hide()

        else:
            self.w2.show()

class Histogramm1(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 800
        self.w1 = HilfeFenster()
        self.w2 = TaschenrechnerFenster()
        self.w3 = HinweiseFenster()
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setFixedSize(1100, 730)
        self.setWindowTitle('Histogram task generator variant 1')
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)


        self.pushbutton_formelsammlung = QtWidgets.QPushButton()
        self.pushbutton_formelsammlung.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #687864; color:#ffffff; font:bold;font-size: 20px;")
        self.pushbutton_formelsammlung.setObjectName("pushbutton_formelsammlung")
        self.pushbutton_formelsammlung.setText("Help")
        self.pushbutton_formelsammlung.clicked.connect(self.formelsammlung_oeffnen)
        self.pushButton_taschenrechner = QtWidgets.QPushButton()
        self.pushButton_taschenrechner.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #687864; color:#ffffff; font:bold;font-size: 20px;")
        self.pushButton_taschenrechner.setObjectName("pushButton_taschenrechner")
        self.pushButton_taschenrechner.setText("Calculator")
        self.pushButton_taschenrechner.clicked.connect(self.taschenrechner_oeffnen)
        self.pushButton_impressum = QtWidgets.QPushButton()
        self.pushButton_impressum.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #687864; color:#ffffff; font:bold;font-size: 20px;")
        self.pushButton_impressum.setObjectName("pushButton_impressum")
        self.pushButton_impressum.setText("Hints on use")
        self.pushButton_impressum.clicked.connect(self.hinweise_oeffnen)

        self.aufgabe = QLabel("aufgabe")
        self.daten = QLabel("daten")
        self.aufgabe.setStyleSheet("color:#31708E;border-color: #31708E;font-size: 20px;")
        self.daten.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        self.aufgabe.setText(("Create a histogram with 4 equidistant classes for the following data:"))
        self.daten.setText("Click on new task")
        self.aufgabe.setStyleSheet("color:#31708E;border-color: #31708E;font-size: 20px;")
        self.daten.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")

        self.button = QPushButton('Solution')
        self.button2 = QPushButton('New task')
        self.button2.clicked.connect(self.newdata)
        self.button.clicked.connect(self.plot)
        self.button2.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #31708E; color:#ffffff; font:bold;font-size: 20px;")
        self.button.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #31708E; color:#ffffff; font:bold;font-size: 20px;")
        self.button3 = QPushButton('Main page')
        self.button3.clicked.connect(self.goMainWindow)
        self.button3.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #31708E; color:#ffffff; font:bold;font-size: 20px;")

        self.klassengrenzen = QLabel("Classes: [")
        self.klassengrenzen.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")

        self.grenze_eins = QLineEdit(self)
        self.grenze_eins.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.grenze_eins.setPlaceholderText('')

        self.g1 = QLabel(", ")
        self.g1.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")


        self.grenze_zwei1 = QLineEdit(self)
        self.grenze_zwei1.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.grenze_zwei1.setPlaceholderText(" ")

        self.g2 = QLabel(") [")
        self.g2.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")

        self.grenze_zwei = QLineEdit(self)
        self.grenze_zwei.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.grenze_zwei.setPlaceholderText(" ")

        self.g3 = QLabel(", ")
        self.g3.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")

        self.grenze_drei1 = QLineEdit(self)
        self.grenze_drei1.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.grenze_drei1.setPlaceholderText(" ")

        self.g4 = QLabel(") [")
        self.g4.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")

        self.grenze_drei = QLineEdit(self)
        self.grenze_drei.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.grenze_drei.setPlaceholderText(" ")

        self.g5 = QLabel(", ")
        self.g5.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")

        self.grenze_vier1 = QLineEdit(self)
        self.grenze_vier1.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.grenze_vier1.setPlaceholderText(" ")

        self.g6 = QLabel(") [")
        self.g6.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")

        self.grenze_vier = QLineEdit(self)
        self.grenze_vier.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.grenze_vier.setPlaceholderText(" ")

        self.g7 = QLabel(", ")
        self.g7.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")

        self.grenze_fuenf = QLineEdit(self)
        self.grenze_fuenf.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.grenze_fuenf.setPlaceholderText(" ")

        self.g8 = QLabel("]")
        self.g8.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")

        self.hoehe_eins = QLineEdit(self)
        self.hoehe_eins.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.hoehe_eins.setPlaceholderText("First class height")

        self.hoehe_zwei = QLineEdit(self)
        self.hoehe_zwei.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.hoehe_zwei.setPlaceholderText("Second class height")

        self.hoehe_drei = QLineEdit(self)
        self.hoehe_drei.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.hoehe_drei.setPlaceholderText("Third class height")

        self.hoehe_vier = QLineEdit(self)
        self.hoehe_vier.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.hoehe_vier.setPlaceholderText("Fourth class height")

        outerLayout = QVBoxLayout()
        mLayout = QHBoxLayout()
        mLayout.addWidget(self.pushbutton_formelsammlung)
        mLayout.addWidget(self.pushButton_taschenrechner)
        mLayout.addWidget(self.pushButton_impressum)
        # topLayout = QHBoxLayout()
        # topLayout.addWidget(self.aufgabe)
        # topLayout.addWidget(self.daten)
        middleLayout = QHBoxLayout()
        middleLayout.addWidget(self.klassengrenzen)
        middleLayout.addWidget(self.grenze_eins)
        middleLayout.addWidget(self.g1)
        middleLayout.addWidget(self.grenze_zwei1)
        middleLayout.addWidget(self.g2)
        middleLayout.addWidget(self.grenze_zwei)
        middleLayout.addWidget(self.g3)
        middleLayout.addWidget(self.grenze_drei1)
        middleLayout.addWidget(self.g4)
        middleLayout.addWidget(self.grenze_drei)
        middleLayout.addWidget(self.g5)
        middleLayout.addWidget(self.grenze_vier1)
        middleLayout.addWidget(self.g6)
        middleLayout.addWidget(self.grenze_vier)
        middleLayout.addWidget(self.g7)
        middleLayout.addWidget(self.grenze_fuenf)
        middleLayout.addWidget(self.g8)
        middleLayout2 = QHBoxLayout()
        middleLayout2.addWidget(self.hoehe_eins)
        middleLayout2.addWidget(self.hoehe_zwei)
        middleLayout2.addWidget(self.hoehe_drei)
        middleLayout2.addWidget(self.hoehe_vier)
        bottomLayout = QHBoxLayout()
        bottomLayout.addWidget(self.button3)
        bottomLayout.addWidget(self.button2)
        bottomLayout.addWidget(self.button)
        outerLayout.addLayout(mLayout)
        outerLayout.addWidget(self.aufgabe)
        outerLayout.addWidget(self.daten)
        # outerLayout.addLayout(topLayout)
        outerLayout.addLayout(middleLayout)
        outerLayout.addLayout(middleLayout2)
        outerLayout.addWidget(self.canvas)
        outerLayout.addLayout(bottomLayout)
        self.setLayout(outerLayout)

    def closeEvent(self, event):
        if self.w1:
            self.w1.close()
        if self.w2:
            self.w2.close()
        if self.w3:
            self.w3.close()

    def goMainWindow(self):
        self.cams = Window()
        self.cams.show()
        self.close()

    def newdata(self):
        rand_mean = (np.random.randint(8, high=20, size=None, dtype=int))
        rand_n = (np.random.randint(15, high=17, size=None, dtype=int))
        data = np.random.normal(rand_mean, rand_mean / 3, rand_n)
        data = data.astype(int)
        data = abs(data)
        data = np.sort(data)
        H = plt.hist(data, bins=4, edgecolor='black')
        # klassenbreite = H[1][1]-H[1][0]
        text = ("Create a histogram with 4 equidistant classes for the following data: (n= "+ str((len(data))) +") :")
        data2 = np.array2string(data, separator=',')
        data2 = (data2[1:-1])
        self.aufgabe.setText(text)
        self.daten.setText((str(data2)))
        self.aufgabe.setStyleSheet("color:#31708E;border-color: #31708E;font-size: 20px;")
        self.daten.setStyleSheet("color:#31708E;border-color: #31708E;font-size: 20px;")

        self.grenze_eins.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.grenze_zwei.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.grenze_drei.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.grenze_vier.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.grenze_zwei1.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.grenze_drei1.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.grenze_vier1.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.grenze_fuenf.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.grenze_eins.setText("")
        self.grenze_zwei.setText("")
        self.grenze_zwei1.setText("")
        self.grenze_drei.setText("")
        self.grenze_drei1.setText("")
        self.grenze_vier.setText("")
        self.grenze_vier1.setText("")
        self.grenze_fuenf.setText("")

        self.grenze_eins.setText(str(H[1][0]))
        self.grenze_eins.setReadOnly(True)
        self.grenze_zwei1.setPlaceholderText("")
        self.grenze_zwei.setPlaceholderText("")
        self.grenze_drei1.setPlaceholderText("")
        self.grenze_drei.setPlaceholderText("")
        self.grenze_vier1.setPlaceholderText("")
        self.grenze_vier.setPlaceholderText("")
        self.grenze_fuenf.setText(str(H[1][4]))
        self.grenze_fuenf.setReadOnly(True)

        self.hoehe_eins.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.hoehe_zwei.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.hoehe_drei.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.hoehe_vier.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.hoehe_eins.setText("")
        self.hoehe_zwei.setText("")
        self.hoehe_drei.setText("")
        self.hoehe_vier.setText("")

        self.hoehe_eins.setPlaceholderText("First class height")
        self.hoehe_zwei.setPlaceholderText("Second class height")
        self.hoehe_drei.setPlaceholderText("Third class height")
        self.hoehe_vier.setPlaceholderText("Fourth class height")
        self.figure.clear()
        plt.draw()

    def formelsammlung_oeffnen(self, checked):
        if self.w1.isVisible():
            self.w1.hide()

        else:
            self.w1.show()

    def hinweise_oeffnen(self):
        if self.w3.isVisible():
            self.w3.hide()

        else:
            self.w3.show()

    def taschenrechner_oeffnen(self):
        if self.w2.isVisible():
            self.w2.hide()

        else:
            self.w2.show()

    def plot(self):

        self.figure.clear()
        # check solution
        try:
            data = self.daten.text()
            data = re.findall(r'\d+', data)
            data = list(map(int, data))
            max(data)
            H = plt.hist(data, bins=4, edgecolor='black', density=True)
            bins = H[1]
            d = H[0]
            hoehe = []
            for x in range(4):
                for x in range(4):
                    hoehe.append(round(d[x], 3))
            # clearing old figure
            self.figure.clear()
            # create an axis
            ax = self.figure.add_subplot(111)
            ax.set(xlabel="x", ylabel="$g_j$")
            # plot data
            ax.hist(data, bins=4, edgecolor='black', density=True)
            # refresh canvas
            self.canvas.draw()
        except:
            self.newdata()
        # check solution
        try:
            if float(self.grenze_eins.text()) == bins[0]:
                self.grenze_eins.setStyleSheet("color:green;font-size: 20px;")
            else:
                self.grenze_eins.setStyleSheet("color:red;font-size: 20px;")
            if float(self.grenze_zwei.text()) == bins[1]:
                self.grenze_zwei.setStyleSheet("color:green;font-size: 20px;")
            else:
                self.grenze_zwei.setStyleSheet("color:red;font-size: 20px;")
            if float(self.grenze_zwei1.text()) == bins[1]:
                self.grenze_zwei1.setStyleSheet("color:green;font-size: 20px;")
            else:
                self.grenze_zwei1.setStyleSheet("color:red;font-size: 20px;")
            if float(self.grenze_drei.text()) == bins[2]:
                self.grenze_drei.setStyleSheet("color:green;font-size: 20px;")
            else:
                self.grenze_drei.setStyleSheet("color:red;font-size: 20px;")
            if float(self.grenze_drei1.text()) == bins[2]:
                self.grenze_drei1.setStyleSheet("color:green;font-size: 20px;")
            else:
                self.grenze_drei1.setStyleSheet("color:red;font-size: 20px;")
            if float(self.grenze_vier.text()) == bins[3]:
                self.grenze_vier.setStyleSheet("color:green;font-size: 20px;")
            else:
                self.grenze_vier.setStyleSheet("color:red;font-size: 20px;")
            if float(self.grenze_vier1.text()) == bins[3]:
                self.grenze_vier1.setStyleSheet("color:green;font-size: 20px;")
            else:
                self.grenze_vier1.setStyleSheet("color:red;font-size: 20px;")
            if float(self.grenze_fuenf.text()) == bins[4]:
                self.grenze_fuenf.setStyleSheet("color:green;font-size: 20px;")
            else:
                self.grenze_fuenf.setStyleSheet("color:red;font-size: 20px;")
            if (hoehe[0] - 0.001) <= float(self.hoehe_eins.text()) <= (hoehe[0] + 0.001):
                self.hoehe_eins.setStyleSheet("color:green;font-size: 20px;")
            else:
                self.hoehe_eins.setStyleSheet("color:red;font-size: 20px;")
            if (hoehe[1] - 0.001) <= float(self.hoehe_zwei.text()) <= (hoehe[1] + 0.001):
                self.hoehe_zwei.setStyleSheet("color:green;font-size: 20px;")
            else:
                self.hoehe_zwei.setStyleSheet("color:red;font-size: 20px;")
            if (hoehe[2] - 0.001) <= float(self.hoehe_drei.text()) <= (hoehe[2] + 0.001):
                self.hoehe_drei.setStyleSheet("color:green;font-size: 20px;")
            else:
                self.hoehe_drei.setStyleSheet("color:red;font-size: 20px;")
            if (hoehe[3] - 0.001) <= float(self.hoehe_vier.text()) <= (hoehe[3] + 0.001):
                self.hoehe_vier.setStyleSheet("color:green;font-size: 20px;")
            else:
                self.hoehe_vier.setStyleSheet("color:red;font-size: 20px;")
        except:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error!")
            dlg.setText(
                "Your answers cannot be evaluated. Enter a value for each field. Also pay attention to the format: 4.5. Round to 3 decimal places. Then you can check your answers again.")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Warning)
            button = dlg.exec()

class Histogramm2(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 800
        self.w1 = HilfeFenster()
        self.w2 = TaschenrechnerFenster()
        self.w3 = HinweiseFenster()
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setFixedSize(1100, 730)
        self.setWindowTitle('Histogram task generator variant 2')
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)


        self.pushbutton_formelsammlung = QtWidgets.QPushButton()
        self.pushbutton_formelsammlung.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #687864; color:#ffffff; font:bold;font-size: 20px;")
        self.pushbutton_formelsammlung.setObjectName("pushbutton_formelsammlung")
        self.pushbutton_formelsammlung.setText("Help")
        self.pushbutton_formelsammlung.clicked.connect(self.formelsammlung_oeffnen)
        self.pushButton_taschenrechner = QtWidgets.QPushButton()
        self.pushButton_taschenrechner.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #687864; color:#ffffff; font:bold;font-size: 20px;")
        self.pushButton_taschenrechner.setObjectName("pushButton_taschenrechner")
        self.pushButton_taschenrechner.setText("Calcuator")
        self.pushButton_taschenrechner.clicked.connect(self.taschenrechner_oeffnen)
        self.pushButton_impressum = QtWidgets.QPushButton()
        self.pushButton_impressum.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #687864; color:#ffffff; font:bold;font-size: 20px;")
        self.pushButton_impressum.setObjectName("pushButton_impressum")
        self.pushButton_impressum.setText("Hints on use")
        self.pushButton_impressum.clicked.connect(self.hinweise_oeffnen)

        self.aufgabe = QLabel("aufgabe")
        self.daten = QLabel("daten")

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        self.aufgabe.setText(("Create a histogram with the given class boundaries for the data:"))
        self.daten.setText("Click on new task")
        self.aufgabe.setStyleSheet("color:#31708E;border-color: #31708E;font-size: 20px;")
        self.daten.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")

        self.button = QPushButton('Solution')
        self.button2 = QPushButton('New task')
        self.button2.clicked.connect(self.newdata)
        self.button.clicked.connect(self.plot)
        self.button2.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #31708E; color:#ffffff; font:bold;font-size: 20px;")
        self.button.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #31708E; color:#ffffff; font:bold;font-size: 20px;")
        self.button3 = QPushButton('Main page')
        self.button3.clicked.connect(self.goMainWindow)
        self.button3.setStyleSheet(
            "border: 1px; border-radius: 6px; background-color: #31708E; color:#ffffff; font:bold;font-size: 20px;")

        self.hoehe_eins = QLineEdit(self)
        self.hoehe_eins.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.hoehe_eins.setPlaceholderText("First class height")

        self.hoehe_zwei = QLineEdit(self)
        self.hoehe_zwei.setStyleSheet("color:#687864;""border-color: #31708E;font-size: 20px;")
        self.hoehe_zwei.setPlaceholderText("Second class height")

        self.hoehe_drei = QLineEdit(self)
        self.hoehe_drei.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.hoehe_drei.setPlaceholderText("Third class height")

        self.hoehe_vier = QLineEdit(self)
        self.hoehe_vier.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
        self.hoehe_vier.setPlaceholderText("Fourth class height")

        outerLayout = QVBoxLayout()
        mLayout = QHBoxLayout()
        mLayout.addWidget(self.pushbutton_formelsammlung)
        mLayout.addWidget(self.pushButton_taschenrechner)
        mLayout.addWidget(self.pushButton_impressum)
        middleLayout2 = QHBoxLayout()
        middleLayout2.addWidget(self.hoehe_eins)
        middleLayout2.addWidget(self.hoehe_zwei)
        middleLayout2.addWidget(self.hoehe_drei)
        middleLayout2.addWidget(self.hoehe_vier)
        bottomLayout = QHBoxLayout()
        bottomLayout.addWidget(self.button3)
        bottomLayout.addWidget(self.button2)
        bottomLayout.addWidget(self.button)
        outerLayout.addLayout(mLayout)
        outerLayout.addWidget(self.aufgabe)
        outerLayout.addWidget(self.daten)
        outerLayout.addLayout(middleLayout2)
        outerLayout.addWidget(self.canvas)
        outerLayout.addLayout(bottomLayout)
        self.setLayout(outerLayout)

    def closeEvent(self, event):
        if self.w1:
            self.w1.close()
        if self.w2:
            self.w2.close()
        if self.w3:
            self.w3.close()

    def goMainWindow(self):
        self.cams = Window()
        self.cams.show()
        self.close()

    def newdata(self):
        while True:
            try:
                rand_n = (np.random.randint(15, high=17, size=None, dtype=int))
                rand_mean = (np.random.randint(12, high=20, size=None, dtype=int))
                data = np.random.normal(rand_mean, rand_mean / 3, rand_n)
                data = data.astype(int)
                r = max(data) - min(data)
                b2 = min(data) + round((r / 4) + 1)
                b3 = min(data) + b2 + round((r - b2) / 3) - 3
                b4 = min(data) + b2 + b3 + (r - (min(data) + b2 + b3))
                if (min(data) == b2 or b2 == b3 or b3 == b4 or b4 == max(data)):
                    continue
                H = plt.hist(data, bins=[min(data), b2, b3, b4, max(data)], edgecolor='black', density=True)
                textgrenzen = "[" + str(min(data)) + ", " + str(b2) + ", " + str(b3) + ", " + str(b4) + ", " + str(
                    max(data)) + "]"
                data = np.sort(data)
                text = (
                            "Create a histogram with the class boundaries " + textgrenzen + " for the data (n= "+ str((len(data))) +") :")
                data2 = np.array2string(data, separator=',')
                data2 = (data2[1:-1])
                self.aufgabe.setText(text)
                self.daten.setText((str(data2)))
                self.aufgabe.setStyleSheet("color:#31708E;border-color: #31708E;font-size: 20px;")
                self.daten.setStyleSheet("color:#31708E;border-color: #31708E;font-size: 20px;")

                self.hoehe_eins.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
                self.hoehe_zwei.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
                self.hoehe_drei.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")
                self.hoehe_vier.setStyleSheet("color:#687864;border-color: #31708E;font-size: 20px;")

                self.hoehe_eins.setText("")
                self.hoehe_zwei.setText("")
                self.hoehe_drei.setText("")
                self.hoehe_vier.setText("")
                text1 = "Height of [" + str(min(data)) + "," + str(b2) + ")"
                text2 = "Height of [" + str(b2) + "," + str(b3) + ")"
                text3 = "Height of [" + str(b3) + "," + str(b4) + ")"
                text4 = "Height of [" + str(b4) + "," + str(max(data)) + "]"
                self.hoehe_eins.setPlaceholderText(text1)
                self.hoehe_zwei.setPlaceholderText(text2)
                self.hoehe_drei.setPlaceholderText(text3)
                self.hoehe_vier.setPlaceholderText(text4)
                self.figure.clear()
                plt.draw()
            except:
                continue
            else:
                break

    # def plot(self, data):
    def plot(self):

        self.figure.clear()
        # check solution
        try:
            data = self.daten.text()
            data = re.findall(r'\d+', data)
            data = list(map(int, data))
            r = max(data) - min(data)
            b2 = min(data) + round((r / 4) + 1)
            b3 = min(data) + b2 + round((r - b2) / 3) - 3
            b4 = min(data) + b2 + b3 + (r - (min(data) + b2 + b3))
            H = plt.hist(data, bins=[min(data), b2, b3, b4, max(data)], edgecolor='black')
            bins = H[1]
            d = H[0]
            klassenbreite = ((H[1][1] - H[1][0]), (H[1][2] - H[1][1]), (H[1][3] - H[1][2]), (H[1][4] - H[1][3]))
            hoehe = []
            for x in range(4):
                hoehe.append(round(d[x] / (len(data) * klassenbreite[x]), 3))

            # clearing old figure
            self.figure.clear()
            # create an axis
            ax = self.figure.add_subplot(111)
            ax.set(xlabel="x", ylabel="")
            # plot data
            ax.hist(data, bins=[min(data), b2, b3, b4, max(data)], edgecolor='black', density=True)
            ax.set(xlabel="x", ylabel="$g_j$")
            # refresh canvas
            self.canvas.draw()
        except:
            self.newdata()
        # check solution
        try:
            if (hoehe[0] - 0.001) <= float(self.hoehe_eins.text()) <= (hoehe[0] + 0.001):
                self.hoehe_eins.setStyleSheet("color:green;font-size: 20px;")
            else:
                self.hoehe_eins.setStyleSheet("color:red;font-size: 20px;")
            if (hoehe[1] - 0.001) <= float(self.hoehe_zwei.text()) <= (hoehe[1] + 0.001):
                self.hoehe_zwei.setStyleSheet("color:green;font-size: 20px;")
            else:
                self.hoehe_zwei.setStyleSheet("color:red;font-size: 20px;")
            if (hoehe[2] - 0.001) <= float(self.hoehe_drei.text()) <= (hoehe[2] + 0.001):
                self.hoehe_drei.setStyleSheet("color:green;font-size: 20px;")
            else:
                self.hoehe_drei.setStyleSheet("color:red;font-size: 20px;")
            if (hoehe[3] - 0.001) <= float(self.hoehe_vier.text()) <= (hoehe[3] + 0.001):
                self.hoehe_vier.setStyleSheet("color:green;font-size: 20px;")
            else:
                self.hoehe_vier.setStyleSheet("color:red;font-size: 20px;")
        except:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error!")
            dlg.setText(
                "Your answers cannot be evaluated. Enter a value for each field. Also pay attention to the format: 4.5. Round to 3 decimal places. Then you can check your answers again.")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Warning)
            button = dlg.exec()

    def formelsammlung_oeffnen(self, checked):
        if self.w1.isVisible():
            self.w1.hide()

        else:
            self.w1.show()

    def hinweise_oeffnen(self):
        if self.w3.isVisible():
            self.w3.hide()

        else:
            self.w3.show()

    def taschenrechner_oeffnen(self):
        if self.w2.isVisible():
            self.w2.hide()

        else:
            self.w2.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
