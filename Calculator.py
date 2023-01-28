from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon, QFont,  QGuiApplication
from PyQt5.QtCore import Qt, pyqtSlot
import sys


CalculatorApp = QApplication(sys.argv)

window = QWidget() 
window.setWindowIcon(QIcon("C:\Shamsiddin Courses\Python Course\Shamsiddin python course\Teacher_Lesson\Icons\\icons8-calculator-144.png"))
window.setWindowTitle("Calculator")

# oyna.setGeometry(200, 200, 800, 300)
window.setFixedSize(372, 499)


amal = QPushButton("+/-", window)
amal.move(0, 430)
amal.setFont(QFont("Colcalos", 30, 20))
amal.setStyleSheet("color:Gray; background-color:White")

one = QPushButton("1", window)
one.move(0, 361)
one.setFont(QFont("Colcalos", 30, 20))
one.setStyleSheet("color:Gray; background-color:White")

Cbutton = QPushButton("C", window)
Cbutton.move(0, 154)
Cbutton.setFont(QFont("Colcalos", 30, 20))
Cbutton.setStyleSheet("color:Orange; background-color:White")

seven = QPushButton("7", window)
seven.move(0, 223)
seven.setFont(QFont("Colcalos", 30, 20))
seven.setStyleSheet("color:Gray; background-color:White")

four = QPushButton("4", window)
four.move(0, 292)
four.setFont(QFont("Colcalos", 30, 20))
four.setStyleSheet("color:Gray; background-color:White")

bracket = QPushButton("⁽⁾", window)
bracket.move(93, 154)
bracket.setFont(QFont("Colcalos", 30, 20))
bracket.setStyleSheet("color:LightSkyBlue; background-color:White")

eight = QPushButton("8", window)
eight.move(93, 223)
eight.setFont(QFont("Colcalos", 30, 20))
eight.setStyleSheet("color:Gray; background-color:White")

five = QPushButton("5", window)
five.move(93, 292)
five.setFont(QFont("Colcalos", 30, 20))
five.setStyleSheet("color:Gray; background-color:White")

two = QPushButton("2", window)
two.move(93, 361)
two.setFont(QFont("Colcalos", 30, 20))
two.setStyleSheet("color:Gray; background-color:White")

zero = QPushButton("0", window)
zero.move(93, 430)
zero.setFont(QFont("Colcalos", 30, 20))
zero.setStyleSheet("color:Gray; background-color:white")

procent = QPushButton("%", window)
procent.move(186, 154)
procent.setFont(QFont("Colcalos", 30, 20))
procent.setStyleSheet("color:LightSkyBlue; background-color:White")

nine = QPushButton("9", window)
nine.move(186, 223)
nine.setFont(QFont("Colcalos", 30, 20))
nine.setStyleSheet("color:Gray; background-color:White")

six = QPushButton("6", window)
six.move(186, 292)
six.setFont(QFont("Colcalos", 30, 20))
six.setStyleSheet("color:Gray; background-color:White")

three = QPushButton("3", window)
three.move(186, 361)
three.setFont(QFont("Colcalos", 30, 20))
three.setStyleSheet("color:Gray; background-color:White")

comma = QPushButton(",", window)
comma.move(186, 430)
comma.setFont(QFont("Colcalos", 30, 20))
comma.setStyleSheet("color:Gray; background-color:White")

cancel = QPushButton("⌫", window)
cancel.move(279, 110)
cancel.setFont(QFont("Colcalos", 15, 5))
cancel.setStyleSheet("color:DimGray; background-color:white")

divide = QPushButton("÷", window)
divide.move(279, 154)
divide.setFont(QFont("Colcalos", 30, 20))
divide.setStyleSheet("color:LightSkyBlue; background-color:white")

multi = QPushButton("x", window)
multi.move(279, 223)
multi.setFont(QFont("Colcalos", 30, 20))
multi.setStyleSheet("color:LightSkyBlue; background-color:white")

minus = QPushButton("‒", window)
minus.move(279, 292)
minus.setFont(QFont("Colcalos", 30, 20))
minus.setStyleSheet("color:LightSkyBlue; background-color:white")


plus = QPushButton("+", window)
plus.move(279, 361)
plus.setFont(QFont("Colcalos", 30, 20))
plus.setStyleSheet("color:LightSkyBlue; background-color:white")


equal = QPushButton("=", window)
equal.move(279, 430)
equal.setFont(QFont("Colcalos", 30, 20))
equal.setStyleSheet("color:white; background-color:LightSkyBlue")


show = QLineEdit(window)
show.setFont(QFont("Colcolas", 20))
show.setGeometry(0, 108, 278, 45)
show.setStyleSheet("color:Black; background-color:LightCyan")

show_result = QLineEdit(window)
# show_result.move(0, 10)
show_result.setFont(QFont("Colcolas", 20))
show_result.setGeometry(0, 1, 370, 108)

# st = eval("45+5")


def plus_action():
    show_result.setText(show_result.text() + "+")

def minus_action():
    show_result.setText(show_result.text() + "-")

def divide_action():
    show_result.setText(show_result.text() + "/")

def multi_action():
    show_result.setText(show_result.text() + "*")

def bracket_action():
    show_result.setText(show_result.text() + "()")

def procent_action():
    show_result.setText(show_result.text() + "%")

def Cbutton_change():
    show_result.setText("")
    show.setText("")

def cancel_func():
    text = show_result.text()
    text = text[:-1]
    show_result.setText(text)

def zero_func():
    show_result.setText(show_result.text() + "0")

def one_func():
    show_result.setText(show_result.text() + "1")

def two_func():
    show_result.setText(show_result.text() + "2")

def three_func():
    show_result.setText(show_result.text() + "3")

def four_func():
    show_result.setText(show_result.text() + "4")

def five_func():
    show_result.setText(show_result.text() + "5")

def six_func():
    show_result.setText(show_result.text() + "6")

def seven_func():
    show_result.setText(show_result.text() + "7")

def eight_func():
    show_result.setText(show_result.text() + "8")

def nine_func():
    show_result.setText(show_result.text() + "9")

def result():
    show.setText(str(equal_func()))

def equal_func():
    st = eval(show_result.text())
    return st

equal.clicked.connect(result)

minus.clicked.connect(minus_action)
plus.clicked.connect(plus_action)
multi.clicked.connect(multi_action)
divide.clicked.connect(divide_action)
procent.clicked.connect(procent_action)
bracket.clicked.connect(bracket_action)
Cbutton.clicked.connect(Cbutton_change)
cancel.clicked.connect(cancel_func)

zero.clicked.connect(zero_func)
one.clicked.connect(one_func)
two.clicked.connect(two_func)
three.clicked.connect(three_func)
four.clicked.connect(four_func)
five.clicked.connect(five_func)
six.clicked.connect(six_func)
seven.clicked.connect(seven_func)
eight.clicked.connect(eight_func)
nine.clicked.connect(nine_func)


window.show()
sys.exit(CalculatorApp.exec_())