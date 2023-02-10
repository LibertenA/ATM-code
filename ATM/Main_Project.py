from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
import json
import random

def J1():
    with open('Пользователи.json', 'rb') as read_file:
        data = json.load(read_file)
        print(type(data))
        print(type(data[0]))
    return data


class Balance(QtWidgets.QMainWindow):
    def __init__(self, user, data):
        super(Balance, self).__init__()
        self.setObjectName("NieRBank")
        self.setFixedSize(453, 630)
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.Main_label = QtWidgets.QLabel(self.centralwidget)
        self.Main_label.setGeometry(QtCore.QRect(0, 0, 453, 630))
        self.Main_label.setText("")
        self.Main_label.setPixmap(QtGui.QPixmap("Menu.png"))
        self.Main_label.setObjectName("Main_label")
        self.label_back = QtWidgets.QLabel(self.centralwidget)
        self.label_back.setGeometry(QtCore.QRect(340, 10, 102, 42))
        self.label_back.setText("")
        self.label_back.setPixmap(QtGui.QPixmap("Buttons.png"))
        self.label_back.setObjectName("label_back")
        self.label_balance = QtWidgets.QLabel(self.centralwidget)
        self.label_balance.setGeometry(QtCore.QRect(100, 300, 253, 30))
        self.label_balance.setText("")
        self.label_balance.setPixmap(QtGui.QPixmap("Buttons.png"))
        self.label_balance.setObjectName("label_balance")
        self.BACK_button = QtWidgets.QPushButton(self.centralwidget)
        self.BACK_button.setGeometry(QtCore.QRect(340, 10, 102, 40))
        self.BACK_button.setText("Назад")
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.BACK_button.setFont(font)
        self.BACK_button.setStyleSheet("color: rgb(0, 0, 0);\n"
"border: none;")
        self.BACK_button.setObjectName("BACK_button")
        self.Balance_label = QtWidgets.QLabel(self.centralwidget)
        self.Balance_label.setGeometry(QtCore.QRect(101, 300, 251, 28))
        self.Balance_label.setText("Ваш баланс")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Balance_label.setFont(font)
        self.Balance_label.setStyleSheet("color: rgb(0, 0, 0);\n"
"border: none;")
        self.Balance_label.setObjectName("Balance_label")
        self.label_money = QtWidgets.QLabel(self.centralwidget)
        self.label_money.setGeometry(QtCore.QRect(111, 230, 230, 50))
        self.label_money.setText("")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_money.setFont(font)
        self.label_money.setStyleSheet("background-color: rgb(108, 108, 108);")
        self.label_money.setObjectName("label_money")
        self.setCentralWidget(self.centralwidget)
        self.user = user
        self.data = data

        self.pushbutton_back()
        self.vstavka_balance()
        QtCore.QMetaObject.connectSlotsByName(self)

    def pushbutton_back(self):
        self.BACK_button.clicked.connect(self.back)

    def back(self):
        self.MainMenu = Main_Menu(self.user, self.data)
        self.MainMenu.show()
        self.close()
        with open("Логи.txt", 'a') as file:
            file.write(f'Пользователь {self.user["card"]} вернулся к главному окну\n')

    def vstavka_balance(self):
        x = str(self.user['balance'])
        self.MONEY(x)

    def MONEY(self, x):
            self.label_money.setText(x)


class VNESTI(QtWidgets.QMainWindow):
    def __init__(self, user, data):
        super(VNESTI, self).__init__()
        self.setObjectName("NieRBank")
        self.setFixedSize(453, 630)
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.Main_label = QtWidgets.QLabel(self.centralwidget)
        self.Main_label.setGeometry(QtCore.QRect(0, 0, 453, 630))
        self.Main_label.setText("")
        self.Main_label.setPixmap(QtGui.QPixmap("Menu.png"))
        self.Main_label.setObjectName("Main_label")
        self.label_back = QtWidgets.QLabel(self.centralwidget)
        self.label_back.setGeometry(QtCore.QRect(340, 10, 102, 42))
        self.label_back.setText("")
        self.label_back.setPixmap(QtGui.QPixmap("Buttons.png"))
        self.label_back.setObjectName("label_back")
        self.label_Snyatb = QtWidgets.QLabel(self.centralwidget)
        self.label_Snyatb.setGeometry(QtCore.QRect(100, 300, 253, 30))
        self.label_Snyatb.setText("")
        self.label_Snyatb.setPixmap(QtGui.QPixmap("Buttons.png"))
        self.label_Snyatb.setObjectName("label_Snyatb")
        self.BACK_button = QtWidgets.QPushButton(self.centralwidget)
        self.BACK_button.setGeometry(QtCore.QRect(340, 10, 102, 40))
        self.BACK_button.setText("Назад")
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.BACK_button.setFont(font)
        self.BACK_button.setStyleSheet("color: rgb(0, 0, 0);\n"
"border: none;")
        self.BACK_button.setObjectName("BACK_button")
        self.Vnesti_button = QtWidgets.QPushButton(self.centralwidget)
        self.Vnesti_button.setGeometry(QtCore.QRect(100, 300, 251, 28))
        self.Vnesti_button.setText("Внести наличные")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Vnesti_button.setFont(font)
        self.Vnesti_button.setStyleSheet("color: rgb(0, 0, 0);\n"
"border: none;")
        self.Vnesti_button.setObjectName("SNYATb_button")
        self.label_money = QtWidgets.QLabel(self.centralwidget)
        self.label_money.setGeometry(QtCore.QRect(110, 230, 230, 50))
        self.label_money.setText("0")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_money.setFont(font)
        self.label_money.setStyleSheet("background-color: rgb(108, 108, 108);")
        self.label_money.setObjectName("label_money")
        self.butn1 = QtWidgets.QPushButton(self.centralwidget)
        self.butn1.setGeometry(QtCore.QRect(30, 370, 130, 61))
        self.butn1.setText("1")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.butn1.setFont(font)
        self.butn1.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.butn1.setObjectName("butn1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 360, 435, 261))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Buttons.png"))
        self.label_2.setObjectName("label_2")
        self.butn2 = QtWidgets.QPushButton(self.centralwidget)
        self.butn2.setGeometry(QtCore.QRect(160, 370, 130, 61))
        self.butn2.setText("2")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.butn2.setFont(font)
        self.butn2.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.butn2.setObjectName("butn2")
        self.butn3 = QtWidgets.QPushButton(self.centralwidget)
        self.butn3.setGeometry(QtCore.QRect(290, 370, 130, 61))
        self.butn3.setText("3")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.butn3.setFont(font)
        self.butn3.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.butn3.setObjectName("butn3")
        self.butn4 = QtWidgets.QPushButton(self.centralwidget)
        self.butn4.setGeometry(QtCore.QRect(30, 431, 130, 61))
        self.butn4.setText("4")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.butn4.setFont(font)
        self.butn4.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.butn4.setObjectName("butn4")
        self.butn7 = QtWidgets.QPushButton(self.centralwidget)
        self.butn7.setGeometry(QtCore.QRect(30, 491, 130, 61))
        self.butn7.setText("7")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.butn7.setFont(font)
        self.butn7.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.butn7.setObjectName("butn7")
        self.butn5 = QtWidgets.QPushButton(self.centralwidget)
        self.butn5.setGeometry(QtCore.QRect(160, 431, 130, 61))
        self.butn5.setText("5")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.butn5.setFont(font)
        self.butn5.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.butn5.setObjectName("butn5")
        self.butn6 = QtWidgets.QPushButton(self.centralwidget)
        self.butn6.setGeometry(QtCore.QRect(290, 431, 130, 61))
        self.butn6.setText("6")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.butn6.setFont(font)
        self.butn6.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.butn6.setObjectName("butn6")
        self.butn8 = QtWidgets.QPushButton(self.centralwidget)
        self.butn8.setGeometry(QtCore.QRect(160, 491, 130, 61))
        self.butn8.setText("8")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.butn8.setFont(font)
        self.butn8.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.butn8.setObjectName("butn8")
        self.butn9 = QtWidgets.QPushButton(self.centralwidget)
        self.butn9.setGeometry(QtCore.QRect(290, 491, 130, 61))
        self.butn9.setText("9")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.butn9.setFont(font)
        self.butn9.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.butn9.setObjectName("butn9")
        self.butn0 = QtWidgets.QPushButton(self.centralwidget)
        self.butn0.setGeometry(QtCore.QRect(160, 551, 130, 61))
        self.butn0.setText("0")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.butn0.setFont(font)
        self.butn0.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.butn0.setObjectName("butn0")
        self.Main_label.raise_()
        self.label_back.raise_()
        self.label_Snyatb.raise_()
        self.BACK_button.raise_()
        self.Vnesti_button.raise_()
        self.label_money.raise_()
        self.label_2.raise_()
        self.butn1.raise_()
        self.butn2.raise_()
        self.butn3.raise_()
        self.butn4.raise_()
        self.butn5.raise_()
        self.butn6.raise_()
        self.butn7.raise_()
        self.butn8.raise_()
        self.butn9.raise_()
        self.butn0.raise_()
        self.setCentralWidget(self.centralwidget)
        self.user = user
        self.data = data

        self.numbers()
        self.pushbutton_back()
        self.Vnesti()
        QtCore.QMetaObject.connectSlotsByName(self)

    def pushbutton_back(self):
        self.BACK_button.clicked.connect(self.back)

    def back(self):
        self.MainMenu = Main_Menu(self.user, self.data)
        self.MainMenu.show()
        self.close()
        with open("Логи.txt", 'a') as file:
            file.write(f'Пользователь {self.user["card"]} вернулся к главному окну\n')

    def numbers(self):
        self.butn0.clicked.connect(lambda: self.write_number(self.butn0.text()))
        self.butn1.clicked.connect(lambda: self.write_number(self.butn1.text()))
        self.butn2.clicked.connect(lambda: self.write_number(self.butn2.text()))
        self.butn3.clicked.connect(lambda: self.write_number(self.butn3.text()))
        self.butn4.clicked.connect(lambda: self.write_number(self.butn4.text()))
        self.butn5.clicked.connect(lambda: self.write_number(self.butn5.text()))
        self.butn6.clicked.connect(lambda: self.write_number(self.butn6.text()))
        self.butn7.clicked.connect(lambda: self.write_number(self.butn7.text()))
        self.butn8.clicked.connect(lambda: self.write_number(self.butn8.text()))
        self.butn9.clicked.connect(lambda: self.write_number(self.butn9.text()))

    def write_number(self, number):
        if self.label_money.text() == "0":
            self.label_money.setText(number)
        else:
            self.label_money.setText(self.label_money.text()+number)

    def Vnesti(self):
        self.Vnesti_button.clicked.connect(lambda: self.vnesenie())

    def vnesenie(self):
        count = int(self.label_money.text())
        if count >= 50 and count % 10 == 0 and (count % 100 == 0 or count % 100 == 50):
            index = -1
            for i in range(len(self.data)):
                if self.data[i]['password'] == self.user['password']:
                    index = i
                    break
            if index != -1:
                self.data[index]['balance']+=count
            json_object = json.dumps(self.data, indent=1)
            with open('Пользователи.json', 'w') as f:
                f.write(json_object)


            Good = QMessageBox()
            Good.setWindowTitle("Успешно")
            Good.setText("Ваши деньги были успешно внесены")
            Good.setIcon(QMessageBox.Information)
            Good.setStandardButtons(QMessageBox.Ok)

            Good.exec_()
            self.MainMenu = Main_Menu(self.user, self.data)
            self.MainMenu.show()
            self.close()
            with open("Логи.txt", 'a') as file:
                file.write(f"Пользователь {self.user['card']} внес {count} рублей\n")
        else:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Нельзя внести такую сумму")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)

            error.exec_()

            self.vnesti = VNESTI(self.data, self.user)
            self.vnesti.show()
            self.close()


class SNYATb(QtWidgets.QMainWindow):
    def __init__(self, user, data):
        super(SNYATb, self).__init__()
        self.setObjectName("NieRBank")
        self.setFixedSize(453, 630)
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.Main_label = QtWidgets.QLabel(self.centralwidget)
        self.Main_label.setGeometry(QtCore.QRect(0, 0, 453, 630))
        self.Main_label.setText("")
        self.Main_label.setPixmap(QtGui.QPixmap("Menu.png"))
        self.Main_label.setObjectName("Main_label")
        self.label_back = QtWidgets.QLabel(self.centralwidget)
        self.label_back.setGeometry(QtCore.QRect(340, 10, 102, 42))
        self.label_back.setText("")
        self.label_back.setPixmap(QtGui.QPixmap("Buttons.png"))
        self.label_back.setObjectName("label_back")
        self.label_Snyatb = QtWidgets.QLabel(self.centralwidget)
        self.label_Snyatb.setGeometry(QtCore.QRect(100, 300, 253, 30))
        self.label_Snyatb.setText("")
        self.label_Snyatb.setPixmap(QtGui.QPixmap("Buttons.png"))
        self.label_Snyatb.setObjectName("label_Snyatb")
        self.BACK_button = QtWidgets.QPushButton(self.centralwidget)
        self.BACK_button.setGeometry(QtCore.QRect(340, 10, 102, 40))
        self.BACK_button.setText("Назад")
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.BACK_button.setFont(font)
        self.BACK_button.setStyleSheet("color: rgb(0, 0, 0);\n"
"border: none;")
        self.BACK_button.setObjectName("BACK_button")
        self.SNYATb_button = QtWidgets.QPushButton(self.centralwidget)
        self.SNYATb_button.setGeometry(QtCore.QRect(100, 300, 251, 28))
        self.SNYATb_button.setText("Снять наличные")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SNYATb_button.setFont(font)
        self.SNYATb_button.setStyleSheet("color: rgb(0, 0, 0);\n"
"border: none;")
        self.SNYATb_button.setObjectName("SNYATb_button")
        self.label_money = QtWidgets.QLabel(self.centralwidget)
        self.label_money.setGeometry(QtCore.QRect(110, 230, 230, 50))
        self.label_money.setText("0")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_money.setFont(font)
        self.label_money.setStyleSheet("background-color: rgb(108, 108, 108);")
        self.label_money.setObjectName("label_money")
        self.butn1 = QtWidgets.QPushButton(self.centralwidget)
        self.butn1.setGeometry(QtCore.QRect(30, 370, 130, 61))
        self.butn1.setText("1")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.butn1.setFont(font)
        self.butn1.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.butn1.setObjectName("butn1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 360, 435, 261))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Buttons.png"))
        self.label_2.setObjectName("label_2")
        self.butn2 = QtWidgets.QPushButton(self.centralwidget)
        self.butn2.setGeometry(QtCore.QRect(160, 370, 130, 61))
        self.butn2.setText("2")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.butn2.setFont(font)
        self.butn2.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.butn2.setObjectName("butn2")
        self.butn3 = QtWidgets.QPushButton(self.centralwidget)
        self.butn3.setGeometry(QtCore.QRect(290, 370, 130, 61))
        self.butn3.setText("3")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.butn3.setFont(font)
        self.butn3.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.butn3.setObjectName("butn3")
        self.butn4 = QtWidgets.QPushButton(self.centralwidget)
        self.butn4.setGeometry(QtCore.QRect(30, 431, 130, 61))
        self.butn4.setText("4")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.butn4.setFont(font)
        self.butn4.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.butn4.setObjectName("butn4")
        self.butn7 = QtWidgets.QPushButton(self.centralwidget)
        self.butn7.setGeometry(QtCore.QRect(30, 491, 130, 61))
        self.butn7.setText("7")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.butn7.setFont(font)
        self.butn7.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.butn7.setObjectName("butn7")
        self.butn5 = QtWidgets.QPushButton(self.centralwidget)
        self.butn5.setGeometry(QtCore.QRect(160, 431, 130, 61))
        self.butn5.setText("5")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.butn5.setFont(font)
        self.butn5.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.butn5.setObjectName("butn5")
        self.butn6 = QtWidgets.QPushButton(self.centralwidget)
        self.butn6.setGeometry(QtCore.QRect(290, 431, 130, 61))
        self.butn6.setText("6")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.butn6.setFont(font)
        self.butn6.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.butn6.setObjectName("butn6")
        self.butn8 = QtWidgets.QPushButton(self.centralwidget)
        self.butn8.setGeometry(QtCore.QRect(160, 491, 130, 61))
        self.butn8.setText("8")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.butn8.setFont(font)
        self.butn8.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.butn8.setObjectName("butn8")
        self.butn9 = QtWidgets.QPushButton(self.centralwidget)
        self.butn9.setGeometry(QtCore.QRect(290, 491, 130, 61))
        self.butn9.setText("9")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.butn9.setFont(font)
        self.butn9.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.butn9.setObjectName("butn9")
        self.butn0 = QtWidgets.QPushButton(self.centralwidget)
        self.butn0.setGeometry(QtCore.QRect(160, 551, 130, 61))
        self.butn0.setText("0")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.butn0.setFont(font)
        self.butn0.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.butn0.setObjectName("butn0")
        self.Main_label.raise_()
        self.label_back.raise_()
        self.label_Snyatb.raise_()
        self.BACK_button.raise_()
        self.SNYATb_button.raise_()
        self.label_money.raise_()
        self.label_2.raise_()
        self.butn1.raise_()
        self.butn2.raise_()
        self.butn3.raise_()
        self.butn4.raise_()
        self.butn5.raise_()
        self.butn6.raise_()
        self.butn7.raise_()
        self.butn8.raise_()
        self.butn9.raise_()
        self.butn0.raise_()
        self.setCentralWidget(self.centralwidget)
        self.user = user
        self.data = data

        self.numbers()
        self.pushbutton_back()
        self.Snyatb()
        QtCore.QMetaObject.connectSlotsByName(self)

    def pushbutton_back(self):
        self.BACK_button.clicked.connect(self.back)

    def back(self):
        self.Mainmenu = Main_Menu(self.user, self.data)
        self.Mainmenu.show()
        self.close()
        with open("Логи.txt", 'a') as file:
            file.write(f'Пользователь {self.user["card"]} вернулся к главному окну\n')

    def numbers(self):
        self.butn0.clicked.connect(lambda: self.write_number(self.butn0.text()))
        self.butn1.clicked.connect(lambda: self.write_number(self.butn1.text()))
        self.butn2.clicked.connect(lambda: self.write_number(self.butn2.text()))
        self.butn3.clicked.connect(lambda: self.write_number(self.butn3.text()))
        self.butn4.clicked.connect(lambda: self.write_number(self.butn4.text()))
        self.butn5.clicked.connect(lambda: self.write_number(self.butn5.text()))
        self.butn6.clicked.connect(lambda: self.write_number(self.butn6.text()))
        self.butn7.clicked.connect(lambda: self.write_number(self.butn7.text()))
        self.butn8.clicked.connect(lambda: self.write_number(self.butn8.text()))
        self.butn9.clicked.connect(lambda: self.write_number(self.butn9.text()))

    def write_number(self, number):
        if self.label_money.text() == "0":
            self.label_money.setText(number)
        else:
            self.label_money.setText(self.label_money.text()+number)

    def Snyatb(self):
        self.SNYATb_button.clicked.connect(lambda: self.Snyatie())

    def Snyatie(self):
        with open("Кассета_1.txt", "r") as file:
            cas_5000 = int(file.readline())
        with open("Кассета_2.txt", "r") as file:
            cas_2000 = int(file.readline())
        with open("Кассета_3.txt", "r") as file:
            cas_1000 = int(file.readline())
        with open("Кассета_4.txt", "r") as file:
            cas_500 = int(file.readline())
        with open("Кассета_5.txt", "r") as file:
            cas_200 = int(file.readline())
        with open("Кассета_6.txt", "r") as file:
            cas_100 = int(file.readline())
        with open("Кассета_7.txt", "r") as file:
            cas_50 = int(file.readline())
        balance = self.user['balance']
        count = int(self.label_money.text())
        if balance>=count:
            if count >= 50 and count % 10 == 0 and (count % 100 == 0 or count % 100 == 50):
                Flag = True
                while count > 0:
                    if count >= 5000 and cas_5000 > 0:
                        count = count - 5000
                        balance = balance - 5000
                        cas_5000 = cas_5000 - 1
                    elif count >= 2000 and cas_2000 > 0:
                        count = count - 2000
                        balance = balance - 2000
                        cas_2000 = cas_2000 - 1
                    elif count >= 1000 and cas_1000 > 0:
                        count = count - 1000
                        balance = balance - 1000
                        cas_1000 = cas_1000 - 1
                    elif count >= 500 and cas_500 > 0:
                        count = count - 500
                        balance = balance - 500
                        cas_500 = cas_500 - 1
                    elif count >= 200 and cas_200 > 0:
                        count = count - 200
                        balance = balance - 200
                        cas_200 = cas_200 - 1
                    elif count >= 100 and cas_100 > 0:
                        count = count - 100
                        balance = balance - 100
                        cas_100 = cas_100 - 1
                    elif count >= 50 and cas_50 > 0:
                        count = count - 50
                        balance = balance - 50
                        cas_50 = cas_50 - 1
                    else:
                        Flag = False
                        error = QMessageBox()
                        error.setWindowTitle("Ошибка")
                        error.setText("Не хватает банкнот! Пожалуйста попробуйте снять другую сумму")
                        error.setIcon(QMessageBox.Warning)
                        error.setStandardButtons(QMessageBox.Ok)
                        error.exec_()

                        self.Snyat = SNYATb()
                        self.Snyat.show()
                        self.close()
                        with open("Логи.txt", 'a') as file:
                            with open("Логи.txt", 'a') as file:
                                file.write(f"Пользователь {self.user['card']} попытался снять {count} рублей\n")
                        break
                if Flag:
                    cas_5000 = str(cas_5000)
                    cas_2000 = str(cas_2000)
                    cas_1000 = str(cas_1000)
                    cas_500 = str(cas_500)
                    cas_200 = str(cas_200)
                    cas_100 = str(cas_100)
                    cas_50 = str(cas_50)

                    with open("Кассета_1.txt", "w+") as file:
                        file.write(cas_5000)
                    with open("Кассета_2.txt", "w+") as file:
                        file.write(cas_2000)
                    with open("Кассета_3.txt", "w+") as file:
                        file.write(cas_1000)
                    with open("Кассета_4.txt", "w+") as file:
                        file.write(cas_500)
                    with open("Кассета_5.txt", "w+") as file:
                        file.write(cas_200)
                    with open("Кассета_6.txt", "w+") as file:
                        file.write(cas_100)
                    with open("Кассета_7.txt", "w+") as file:
                        file.write(cas_50)

                    index = -1
                    for i in range(len(self.data)):
                        if self.data[i]['password'] == self.user['password']:
                            index = i
                            break
                    if index != -1:
                        self.data[index]['balance'] = balance - count
                    json_object = json.dumps(self.data, indent=1)
                    with open('Пользователи.json', 'w') as f:
                        f.write(json_object)
                    Good = QMessageBox()
                    Good.setWindowTitle("Успешно")
                    Good.setText("Ваши деньги были успешно сняты")
                    Good.setIcon(QMessageBox.Information)
                    Good.setStandardButtons(QMessageBox.Ok)

                    Good.exec_()
                    self.MainMenu = Main_Menu(self.user, self.data)
                    self.MainMenu.show()
                    self.close()
                    with open("Логи.txt", 'a') as file:
                        file.write(f"Пользователь {self.user['card']} снял {count} рублей\n")
            else:
                error = QMessageBox()
                error.setWindowTitle("Ошибка")
                error.setText("Нельзя снять такую сумму")
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Ok)

                error.exec_()

                self.Snyat = SNYATb(self.user, self.data)
                self.Snyat.show()
                self.close()
                with open("Логи.txt", 'a') as file:
                    file.write(f"Пользователь {self.user['card']} попытался снять {count} рублей\n")
        else:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Не хватает денег на вашем балансе! Попробуйте ещё раз")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()

            self.Snyat = SNYATb(self.user, self.data)
            self.Snyat.show()
            self.close()
            with open("Логи.txt", 'a') as file:
                file.write(f"Пользователь {self.user['card']} попытался снять {count} рублей\n")


class Logi(QtWidgets.QMainWindow):
    def __init__(self, user, data):
        super(Logi, self).__init__()
        self.setObjectName("MainWindow")
        self.setFixedSize(453, 633)
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.Main_label = QtWidgets.QLabel(self.centralwidget)
        self.Main_label.setGeometry(QtCore.QRect(0, 0, 453, 641))
        self.Main_label.setText("")
        self.Main_label.setPixmap(QtGui.QPixmap("Menu.png"))
        self.Main_label.setObjectName("Main_label")
        self.label_back = QtWidgets.QLabel(self.centralwidget)
        self.label_back.setGeometry(QtCore.QRect(340, 10, 102, 42))
        self.label_back.setText("")
        self.label_back.setPixmap(QtGui.QPixmap("Buttons.png"))
        self.label_back.setObjectName("label_back")
        self.BACK_button = QtWidgets.QPushButton(self.centralwidget)
        self.BACK_button.setGeometry(QtCore.QRect(340, 10, 102, 40))
        self.BACK_button.setText("Назад")
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.BACK_button.setFont(font)
        self.BACK_button.setStyleSheet("color: rgb(0, 0, 0);\n"
"border: none;")
        self.BACK_button.setObjectName("BACK_button")
        self.label_dark = QtWidgets.QLabel(self.centralwidget)
        self.label_dark.setGeometry(QtCore.QRect(10, 100, 431, 490))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_dark.setFont(font)
        self.label_dark.setText("")
        self.label_dark.setPixmap(QtGui.QPixmap("Dark background.png"))
        self.label_dark.setScaledContents(True)
        self.label_dark.setObjectName("label_dark")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(10, 60, 91, 31))
        self.label_name.setText("Логи")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.logi = QtWidgets.QTextEdit(self.centralwidget)
        self.logi.setGeometry(QtCore.QRect(10, 100, 431, 490))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.logi.setFont(font)
        self.logi.setStyleSheet("border: none;\n"
"color: rgb(0, 0, 0);")
        self.logi.setText("")
        self.logi.setObjectName("label_logi")
        self.setCentralWidget(self.centralwidget)
        self.label_0 = QtWidgets.QLabel(self.centralwidget)
        self.label_0.setGeometry(QtCore.QRect(340, 591, 102, 42))
        self.label_0.setText("")
        self.label_0.setPixmap(QtGui.QPixmap("Dark background.png"))
        self.label_0.setObjectName("label_back")
        self.Obnulitb_button = QtWidgets.QPushButton(self.centralwidget)
        self.Obnulitb_button.setGeometry(QtCore.QRect(340, 591, 102, 40))
        self.Obnulitb_button.setText("Обнулить")
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Obnulitb_button.setFont(font)
        self.Obnulitb_button.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: none;")
        self.Obnulitb_button.setObjectName("Obnulitb_button")
        self.user = user
        self.data = data

        self.pushbutton_back()
        self.LOGI()
        self.obnulenie()
        QtCore.QMetaObject.connectSlotsByName(self)

    def pushbutton_back(self):
        self.BACK_button.clicked.connect(self.back)

    def back(self):
        self.ad = Admin(self.user, self.data)
        self.ad.show()
        self.close()

    def LOGI(self):
        with open("Логи.txt", "r") as file:
            x = file.read()
        self.logi.setText(x)
        self.logi.setReadOnly(True)
        self.logi.moveCursor(QtGui.QTextCursor.End)

    def obnulenie(self):
        self.Obnulitb_button.clicked.connect(self.obnul)

    def obnul(self):
        with open("Логи.txt", 'w') as file:
            file.close()
        self.logi.setText('')
        self.logi.setReadOnly(True)
        self.logi.moveCursor(QtGui.QTextCursor.End)


class Kasseta(QtWidgets.QMainWindow):
    def __init__(self, user, data):
        super(Kasseta, self).__init__()
        self.setObjectName("NieRBank")
        self.setFixedSize(453, 633)
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.Main_label = QtWidgets.QLabel(self.centralwidget)
        self.Main_label.setGeometry(QtCore.QRect(0, 0, 453, 641))
        self.Main_label.setText("")
        self.Main_label.setPixmap(QtGui.QPixmap("Menu.png"))
        self.Main_label.setObjectName("Main_label")
        self.label_back = QtWidgets.QLabel(self.centralwidget)
        self.label_back.setGeometry(QtCore.QRect(340, 10, 102, 42))
        self.label_back.setText("")
        self.label_back.setPixmap(QtGui.QPixmap("Buttons.png"))
        self.label_back.setObjectName("label_back")
        self.BACK_button = QtWidgets.QPushButton(self.centralwidget)
        self.BACK_button.setGeometry(QtCore.QRect(340, 10, 102, 40))
        self.BACK_button.setText("Назад")
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.BACK_button.setFont(font)
        self.BACK_button.setStyleSheet("color: rgb(0, 0, 0);\n"
"border: none;")
        self.BACK_button.setObjectName("BACK_button")
        self.label_5000 = QtWidgets.QLabel(self.centralwidget)
        self.label_5000.setGeometry(QtCore.QRect(0, 90, 201, 50))
        self.label_5000.setText("Кассета №1(ном. 5000):")
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5000.setFont(font)
        self.label_5000.setObjectName("label_5000")
        self.label_2000 = QtWidgets.QLabel(self.centralwidget)
        self.label_2000.setGeometry(QtCore.QRect(0, 155, 201, 50))
        self.label_2000.setText("Кассета №2(ном. 2000):")
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2000.setFont(font)
        self.label_2000.setObjectName("label_2000")
        self.label_1000 = QtWidgets.QLabel(self.centralwidget)
        self.label_1000.setGeometry(QtCore.QRect(0, 220, 201, 50))
        self.label_1000.setText("Кассета №3(ном. 1000):")
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_1000.setFont(font)
        self.label_1000.setObjectName("label_1000")
        self.label_500 = QtWidgets.QLabel(self.centralwidget)
        self.label_500.setGeometry(QtCore.QRect(0, 280, 191, 50))
        self.label_500.setText("Кассета №4(ном. 500):")
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_500.setFont(font)
        self.label_500.setObjectName("label_500")
        self.label_200 = QtWidgets.QLabel(self.centralwidget)
        self.label_200.setGeometry(QtCore.QRect(0, 340, 191, 50))
        self.label_200.setText("Кассета №5(ном. 200):")
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_200.setFont(font)
        self.label_200.setObjectName("label_200")
        self.label_100 = QtWidgets.QLabel(self.centralwidget)
        self.label_100.setGeometry(QtCore.QRect(0, 400, 191, 50))
        self.label_100.setText("Кассета №6(ном. 100):")
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_100.setFont(font)
        self.label_100.setObjectName("label_100")
        self.label_50 = QtWidgets.QLabel(self.centralwidget)
        self.label_50.setGeometry(QtCore.QRect(0, 460, 181, 50))
        self.label_50.setText("Кассета №7(ном. 50):")
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_50.setFont(font)
        self.label_50.setObjectName("label_50")
        self.lbl_5000 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_5000.setGeometry(QtCore.QRect(200, 100, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_5000.setFont(font)
        self.lbl_5000.setText("")
        self.lbl_5000.setObjectName("lbl_5000")
        self.lbl_2000 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_2000.setGeometry(QtCore.QRect(200, 165, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_2000.setFont(font)
        self.lbl_2000.setText("")
        self.lbl_2000.setObjectName("lbl_2000")
        self.lbl_1000 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_1000.setGeometry(QtCore.QRect(200, 230, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_1000.setFont(font)
        self.lbl_1000.setText("")
        self.lbl_1000.setObjectName("lbl_1000")
        self.lbl_500 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_500.setGeometry(QtCore.QRect(190, 290, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_500.setFont(font)
        self.lbl_500.setText("")
        self.lbl_500.setObjectName("lbl_500")
        self.lbl_200 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_200.setGeometry(QtCore.QRect(190, 350, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_200.setFont(font)
        self.lbl_200.setText("")
        self.lbl_200.setObjectName("lbl_200")
        self.lbl_100 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_100.setGeometry(QtCore.QRect(190, 410, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_100.setFont(font)
        self.lbl_100.setText("")
        self.lbl_100.setObjectName("lbl_100")
        self.lbl_50 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_50.setGeometry(QtCore.QRect(180, 470, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_50.setFont(font)
        self.lbl_50.setText("")
        self.lbl_50.setObjectName("lbl_50")

        self.pushButton_5000 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5000.setGeometry(QtCore.QRect(310, 110, 111, 31))
        self.pushButton_5000.setText("Заполнить")
        self.pushButton_5000.setStyleSheet("background-color: rgb(113, 113, 113);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_5000.setObjectName("pushButton_5000")
        self.pushButton_2000 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2000.setGeometry(QtCore.QRect(310, 175, 111, 31))
        self.pushButton_2000.setText("Заполнить")
        self.pushButton_2000.setStyleSheet("background-color: rgb(113, 113, 113);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2000.setObjectName("pushButton_2000")
        self.pushButton_200 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_200.setText("Заполнить")
        self.pushButton_200.setGeometry(QtCore.QRect(310, 360, 111, 31))
        self.pushButton_200.setStyleSheet("background-color: rgb(113, 113, 113);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_200.setObjectName("pushButton_200")
        self.pushButton_50 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_50.setGeometry(QtCore.QRect(310, 480, 111, 31))
        self.pushButton_50.setText("Заполнить")
        self.pushButton_50.setStyleSheet("background-color: rgb(113, 113, 113);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_50.setObjectName("pushButton_50")
        self.pushButton_1000 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1000.setGeometry(QtCore.QRect(310, 240, 111, 31))
        self.pushButton_1000.setText("Заполнить")
        self.pushButton_1000.setStyleSheet("background-color: rgb(113, 113, 113);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_1000.setObjectName("pushButton_1000")
        self.pushButton_500 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_500.setGeometry(QtCore.QRect(310, 300, 111, 31))
        self.pushButton_500.setText("Заполнить")
        self.pushButton_500.setStyleSheet("background-color: rgb(113, 113, 113);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_500.setObjectName("pushButton_500")
        self.pushButton_100 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_100.setGeometry(QtCore.QRect(310, 420, 111, 31))
        self.pushButton_100.setText("Заполнить")
        self.pushButton_100.setStyleSheet("background-color: rgb(113, 113, 113);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_100.setObjectName("pushButton_100")
        self.setCentralWidget(self.centralwidget)
        self.user = user
        self.data = data

        self.pushbutton_back()
        self.pushbutton_kas()
        self.obzor()
        QtCore.QMetaObject.connectSlotsByName(self)

    def pushbutton_back(self):
        self.BACK_button.clicked.connect(self.back)

    def back(self):
        self.admin = Admin(self.user, self.data)
        self.admin.show()
        self.close()

    def obzor(self):
        with open("Кассета_1.txt", "r") as file:
            cas_5000 = file.readline()
        with open("Кассета_2.txt", "r") as file:
            cas_2000 = file.readline()
        with open("Кассета_3.txt", "r") as file:
            cas_1000 = file.readline()
        with open("Кассета_4.txt", "r") as file:
            cas_500 = file.readline()
        with open("Кассета_5.txt", "r") as file:
            cas_200 = file.readline()
        with open("Кассета_6.txt", "r") as file:
            cas_100 = file.readline()
        with open("Кассета_7.txt", "r") as file:
            cas_50 = file.readline()
        self.lbl_5000.setText(cas_5000)
        self.lbl_2000.setText(cas_2000)
        self.lbl_1000.setText(cas_1000)
        self.lbl_500.setText(cas_500)
        self.lbl_200.setText(cas_200)
        self.lbl_100.setText(cas_100)
        self.lbl_50.setText(cas_50)

    def pushbutton_kas(self):
        self.pushButton_5000.clicked.connect(self.zapolnenie_5000)
        self.pushButton_2000.clicked.connect(self.zapolnenie_2000)
        self.pushButton_1000.clicked.connect(self.zapolnenie_1000)
        self.pushButton_500.clicked.connect(self.zapolnenie_500)
        self.pushButton_200.clicked.connect(self.zapolnenie_200)
        self.pushButton_100.clicked.connect(self.zapolnenie_100)
        self.pushButton_50.clicked.connect(self.zapolnenie_50)

    def zapolnenie_5000(self):
        if int(self.lbl_5000.text()) <= 2500:
            self.lbl_5000.setText(str(2500))
            with open("Кассета_1.txt", "w") as file:
                file.write((str(2500)))
        else:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Кассета и так заполнена!")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)

            error.exec_()

    def zapolnenie_2000(self):
        if int(self.lbl_2000.text()) <= 2500:
            self.lbl_2000.setText(str(2500))
            with open("Кассета_2.txt", "w") as file:
                file.write((str(2500)))
        else:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Кассета и так заполнена!")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()

    def zapolnenie_1000(self):
        if int(self.lbl_1000.text()) <= 2500:
            self.lbl_1000.setText(str(2500))
            with open("Кассета_3.txt", "w") as file:
                file.write((str(2500)))
        else:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Кассета и так заполнена!")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()

    def zapolnenie_500(self):
        if int(self.lbl_500.text()) <= 2500:
            self.lbl_500.setText(str(2500))
            with open("Кассета_4.txt", "w") as file:
                file.write((str(2500)))
        else:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Кассета и так заполнена!")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()

    def zapolnenie_200(self):
        if int(self.lbl_200.text()) <= 2500:
            self.lbl_200.setText(str(2500))
            with open("Кассета_5.txt", "w") as file:
                file.write((str(2500)))
        else:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Кассета и так заполнена!")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()

    def zapolnenie_100(self):
        if int(self.lbl_100.text()) <= 2500:
            self.lbl_100.setText(str(2500))
            with open("Кассета_6.txt", "w") as file:
                file.write((str(2500)))
        else:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Кассета и так заполнена!")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()

    def zapolnenie_50(self):
        if int(self.lbl_50.text()) <= 2500:
            self.lbl_50.setText(str(2500))
            with open("Кассета_7.txt", "w") as file:
                file.write((str(2500)))
        else:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Кассета и так заполнена!")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()


class Admin(QtWidgets.QMainWindow):
    def __init__(self, user, data):
        super(Admin, self).__init__()
        self.setObjectName("NieRBank")
        self.setFixedSize(453, 630)
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.Main_label = QtWidgets.QLabel(self.centralwidget)
        self.Main_label.setGeometry(QtCore.QRect(0, 0, 453, 630))
        self.Main_label.setText("")
        self.Main_label.setPixmap(QtGui.QPixmap("Menu.png"))
        self.Main_label.setObjectName("Main_label")
        self.label_back = QtWidgets.QLabel(self.centralwidget)
        self.label_back.setGeometry(QtCore.QRect(340, 10, 102, 42))
        self.label_back.setText("")
        self.label_back.setPixmap(QtGui.QPixmap("Buttons.png"))
        self.label_back.setObjectName("label_back")
        self.label_continue = QtWidgets.QLabel(self.centralwidget)
        self.label_continue.setGeometry(QtCore.QRect(10, 240, 432, 181))
        self.label_continue.setText("")
        self.label_continue.setPixmap(QtGui.QPixmap("Buttons.png"))
        self.label_continue.setObjectName("label_continue")
        self.BACK_button = QtWidgets.QPushButton(self.centralwidget)
        self.BACK_button.setGeometry(QtCore.QRect(340, 10, 102, 40))
        self.BACK_button.setText("Назад")
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.BACK_button.setFont(font)
        self.BACK_button.setStyleSheet("color: rgb(0, 0, 0);\n"
"border: none;")
        self.BACK_button.setObjectName("BACK_button")
        self.CASSET_Button = QtWidgets.QPushButton(self.centralwidget)
        self.CASSET_Button.setGeometry(QtCore.QRect(10, 240, 431, 181))
        self.CASSET_Button.setText("Проверка кассет")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.CASSET_Button.setFont(font)
        self.CASSET_Button.setStyleSheet("color: rgb(0, 0, 0);\n"
"border: none;")
        self.CASSET_Button.setObjectName("Continue_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 230, 461, 261))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Dark background.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_continue_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_continue_2.setGeometry(QtCore.QRect(10, 440, 432, 41))
        self.label_continue_2.setText("")
        self.label_continue_2.setPixmap(QtGui.QPixmap("Buttons.png"))
        self.label_continue_2.setObjectName("label_continue_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 440, 432, 42))
        self.pushButton.setText("Логи")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border: none;")
        self.pushButton.setObjectName("pushButton")
        self.Main_label.raise_()
        self.label.raise_()
        self.label_back.raise_()
        self.label_continue.raise_()
        self.BACK_button.raise_()
        self.CASSET_Button.raise_()
        self.label_continue_2.raise_()
        self.pushButton.raise_()
        self.setCentralWidget(self.centralwidget)
        self.user = user
        self.data = data


        self.k_Logam()
        self.pushbutton_back()
        self.k_Kassetam()
        QtCore.QMetaObject.connectSlotsByName(self)

    def pushbutton_back(self):
        self.BACK_button.clicked.connect(self.back)

    def back(self):
        self.Mainmenu = Main_Menu(self.user, self.data)
        self.Mainmenu.show()
        self.close()

    def k_Kassetam(self):
        self.CASSET_Button.clicked.connect(self.Kass)

    def Kass(self):
        self.kass = Kasseta(self.user, self.data)
        self.kass.show()
        self.close()

    def k_Logam(self):
        self.pushButton.clicked.connect(self.Log)

    def Log(self):
        self.log = Logi(self.user, self.data)
        self.log.show()
        self.close()


class Login(QtWidgets.QMainWindow):
    def __init__(self, user, data):
        super(Login, self).__init__()
        self.setObjectName("NieRBank")
        self.setFixedSize(453, 630)
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.Main_label = QtWidgets.QLabel(self.centralwidget)
        self.Main_label.setGeometry(QtCore.QRect(0, 0, 453, 630))
        self.Main_label.setText("")
        self.Main_label.setPixmap(QtGui.QPixmap("Menu.png"))
        self.Main_label.setObjectName("Main_label")
        self.label_back = QtWidgets.QLabel(self.centralwidget)
        self.label_back.setGeometry(QtCore.QRect(340, 10, 102, 42))
        self.label_back.setText("")
        self.label_back.setPixmap(QtGui.QPixmap("Buttons.png"))
        self.label_back.setObjectName("label_back")
        self.label_continue = QtWidgets.QLabel(self.centralwidget)
        self.label_continue.setGeometry(QtCore.QRect(100, 300, 253, 30))
        self.label_continue.setText("")
        self.label_continue.setPixmap(QtGui.QPixmap("Buttons.png"))
        self.label_continue.setObjectName("label_continue")
        self.BACK_button = QtWidgets.QPushButton(self.centralwidget)
        self.BACK_button.setGeometry(QtCore.QRect(340, 10, 102, 40))
        self.BACK_button.setText("Назад")
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.BACK_button.setFont(font)
        self.BACK_button.setStyleSheet("color: rgb(0, 0, 0);\n"
"border: none;")
        self.BACK_button.setObjectName("BACK_button")
        self.Continue_button = QtWidgets.QPushButton(self.centralwidget)
        self.Continue_button.setGeometry(QtCore.QRect(101, 300, 251, 28))
        self.Continue_button.setText("Далее")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Continue_button.setFont(font)
        self.Continue_button.setStyleSheet("color: rgb(0, 0, 0);\n"
"border: none;")
        self.Continue_button.setObjectName("Continue_button")
        self.Login = QtWidgets.QLineEdit(self.centralwidget)
        self.Login.setGeometry(QtCore.QRect(111, 250, 230, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Login.setFont(font)
        self.Login.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(107, 107, 107);")
        self.Login.setObjectName("Login")
        self.setCentralWidget(self.centralwidget)
        self.user = user
        self.data = data

        self.pushbutton_back()
        self.Dalee()
        QtCore.QMetaObject.connectSlotsByName(self)

    def pushbutton_back(self):
        self.BACK_button.clicked.connect(self.back)

    def back(self):
        self.MainMenu = Main_Menu(self.user, self.data)
        self.MainMenu.show()
        self.close()

    def Dalee(self):
        self.Continue_button.clicked.connect(self.Continue_check)

    def Continue_check(self):
        if self.Login.text() == "VSUET":
            self.admin = Admin(self.user, self.data)
            self.admin.show()
            self.close()
        else:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Неправильный логин")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)

            error.exec_()


class Main_Menu(QtWidgets.QMainWindow):
    def __init__(self, user, data):
        super(Main_Menu, self).__init__()
        self.setWindowTitle("NieRBank")
        self.setFixedSize(453, 630)
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.Main_menu = QtWidgets.QLabel(self.centralwidget)
        self.Main_menu.setGeometry(QtCore.QRect(0, 0, 453, 741))
        self.Main_menu.setText("")
        self.Main_menu.setPixmap(QtGui.QPixmap("Menu.png"))
        self.Main_menu.setScaledContents(True)
        self.Main_menu.setObjectName("Main_menu")
        self.END = QtWidgets.QPushButton(self.centralwidget)
        self.END.setGeometry(QtCore.QRect(345, 17, 93, 28))
        self.END.setText("Завершить")
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.END.setFont(font)
        self.END.setAutoFillBackground(False)
        self.END.setStyleSheet("background-color: rgb(255, 255, 255, 0);\n"
"border: none; ")
        self.END.setObjectName("END")
        self.Label_END = QtWidgets.QLabel(self.centralwidget)
        self.Label_END.setGeometry(QtCore.QRect(340, 10, 102, 42))
        self.Label_END.setText("")
        self.Label_END.setPixmap(QtGui.QPixmap("Buttons.png"))
        self.Label_END.setObjectName("Label_END")
        self.DARK = QtWidgets.QLabel(self.centralwidget)
        self.DARK.setGeometry(QtCore.QRect(10, 350, 433, 271))
        self.DARK.setText("")
        self.DARK.setPixmap(QtGui.QPixmap("Buttons.png"))
        self.DARK.setScaledContents(True)
        self.DARK.setObjectName("DARK")
        self.BLACK = QtWidgets.QLabel(self.centralwidget)
        self.BLACK.setGeometry(QtCore.QRect(20, 370, 411, 231))
        self.BLACK.setText("")
        self.BLACK.setPixmap(QtGui.QPixmap("Dark background.png"))
        self.BLACK.setObjectName("BLACK")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(214, 370, 221, 81))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Buttons.png"))
        self.label.setObjectName("label")
        self.label_DrSumma = QtWidgets.QLabel(self.centralwidget)
        self.label_DrSumma.setGeometry(QtCore.QRect(30, 540, 391, 51))
        self.label_DrSumma.setText("")
        self.label_DrSumma.setPixmap(QtGui.QPixmap("LiGHT.png"))
        self.label_DrSumma.setObjectName("label_DrSumma")
        self.label_900 = QtWidgets.QLabel(self.centralwidget)
        self.label_900.setGeometry(QtCore.QRect(33, 470, 121, 51))
        self.label_900.setText("")
        self.label_900.setPixmap(QtGui.QPixmap("LiGHT.png"))
        self.label_900.setObjectName("label_900")
        self.label_2500 = QtWidgets.QLabel(self.centralwidget)
        self.label_2500.setGeometry(QtCore.QRect(165, 470, 121, 51))
        self.label_2500.setText("")
        self.label_2500.setPixmap(QtGui.QPixmap("LiGHT.png"))
        self.label_2500.setObjectName("label_2500")
        self.label_24400 = QtWidgets.QLabel(self.centralwidget)
        self.label_24400.setGeometry(QtCore.QRect(297, 470, 121, 51))
        self.label_24400.setText("")
        self.label_24400.setPixmap(QtGui.QPixmap("LiGHT.png"))
        self.label_24400.setObjectName("label_24400")
        self.pushButton_900 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_900.setGeometry(QtCore.QRect(30, 470, 121, 51))
        self.pushButton_900.setText("900")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_900.setFont(font)
        self.pushButton_900.setStyleSheet("color: rgb(0, 0, 0);\n"
"border: none;")
        self.pushButton_900.setObjectName("pushButton_900")
        self.label_snyatb = QtWidgets.QLabel(self.centralwidget)
        self.label_snyatb.setGeometry(QtCore.QRect(30, 385, 171, 51))
        self.label_snyatb.setText("Cнять")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_snyatb.setFont(font)
        self.label_snyatb.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: none;")
        self.label_snyatb.setObjectName("label_snyatb")
        self.DrSumma = QtWidgets.QPushButton(self.centralwidget)
        self.DrSumma.setGeometry(QtCore.QRect(30, 540, 391, 51))
        self.DrSumma.setText("Другая сумма")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.DrSumma.setFont(font)
        self.DrSumma.setStyleSheet("color: rgb(0, 0, 0);\n"
"border: none;")
        self.DrSumma.setObjectName("DrSumma")
        self.pushButton_2500 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2500.setGeometry(QtCore.QRect(165, 470, 121, 51))
        self.pushButton_2500.setText("2500")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2500.setFont(font)
        self.pushButton_2500.setStyleSheet("color: rgb(0, 0, 0);\n"
"border: none;")
        self.pushButton_2500.setObjectName("pushButton_2500")
        self.pushButton_24400 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_24400.setGeometry(QtCore.QRect(295, 470, 121, 51))
        self.pushButton_24400.setText("24400")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_24400.setFont(font)
        self.pushButton_24400.setStyleSheet("color: rgb(0, 0, 0);\n"
"border: none;")
        self.pushButton_24400.setObjectName("pushButton_24400")
        self.label_Admin = QtWidgets.QLabel(self.centralwidget)
        self.label_Admin.setGeometry(QtCore.QRect(10, 10, 58, 51))
        self.label_Admin.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: none;")
        self.label_Admin.setText("")
        self.label_Admin.setPixmap(QtGui.QPixmap("Buttons.png"))
        self.label_Admin.setObjectName("label_Admin")
        self.Admin = QtWidgets.QPushButton(self.centralwidget)
        self.Admin.setGeometry(QtCore.QRect(10, 10, 61, 51))
        self.Admin.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: none;")
        self.Admin.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("admin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Admin.setIcon(icon)
        self.Admin.setIconSize(QtCore.QSize(50, 50))
        self.Admin.setObjectName("Admin")
        self.label_Vnesti = QtWidgets.QLabel(self.centralwidget)
        self.label_Vnesti.setGeometry(QtCore.QRect(225, 370, 200, 71))
        self.label_Vnesti.setText("")
        self.label_Vnesti.setPixmap(QtGui.QPixmap("LiGHT.png"))
        self.label_Vnesti.setScaledContents(True)
        self.label_Vnesti.setObjectName("label_Vnesti")
        self.VNESTI = QtWidgets.QPushButton(self.centralwidget)
        self.VNESTI.setGeometry(QtCore.QRect(230, 370, 191, 71))
        self.VNESTI.setText("Внести")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.VNESTI.setFont(font)
        self.VNESTI.setStyleSheet("color: rgb(0, 0, 0);\n"
"border: none;")
        self.VNESTI.setObjectName("VNESTI")
        self.label_balance = QtWidgets.QLabel(self.centralwidget)
        self.label_balance.setGeometry(QtCore.QRect(10, 290, 433, 51))
        self.label_balance.setText("")
        self.label_balance.setPixmap(QtGui.QPixmap("Buttons.png"))
        self.label_balance.setObjectName("label_balance")
        self.Balance = QtWidgets.QPushButton(self.centralwidget)
        self.Balance.setGeometry(QtCore.QRect(10, 287, 433, 53))
        self.Balance.setText("Показать баланс")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Balance.setFont(font)
        self.Balance.setStyleSheet("color: rgb(0, 0, 0);\n"
"border: none;")
        self.Balance.setObjectName("Balance")
        self.Main_menu.raise_()
        self.DARK.raise_()
        self.BLACK.raise_()
        self.Label_END.raise_()
        self.END.raise_()
        self.label.raise_()
        self.label_DrSumma.raise_()
        self.label_900.raise_()
        self.label_2500.raise_()
        self.label_24400.raise_()
        self.pushButton_900.raise_()
        self.label_snyatb.raise_()
        self.DrSumma.raise_()
        self.pushButton_2500.raise_()
        self.pushButton_24400.raise_()
        self.label_Admin.raise_()
        self.Admin.raise_()
        self.label_Vnesti.raise_()
        self.VNESTI.raise_()
        self.label_balance.raise_()
        self.Balance.raise_()
        self.setCentralWidget(self.centralwidget)
        self.user = user
        self.data = data

        self.button_Admin()
        self.button_Balance()
        self.button_SNYATb()
        self.Snyatb_900()
        self.Snyatb_2500()
        self.Snyatb_24400()
        self.button_VNESTI()
        self.button_END()
        QtCore.QMetaObject.connectSlotsByName(self)

    def button_END(self):
        self.END.clicked.connect(self.end)

    def end(self):
        self.BeginWindow = Begin_Window(self.data)
        self.BeginWindow.show()
        self.close()
        with open("Логи.txt", 'a') as file:
            file.write(f'Пользователь {self.user["card"]} закончил использование банкомата\n')

    def button_Admin(self):
        self.Admin.clicked.connect(self.Ad)

    def Ad(self):
        self.Adm = Login(self.user, self.data)
        self.Adm.show()
        self.close()

    def button_SNYATb(self):
        self.DrSumma.clicked.connect(self.Drsumma)

    def Drsumma(self):
        self.SNYATb = SNYATb(self.user, self.data)
        self.SNYATb.show()
        self.close()
        with open("Логи.txt", 'a') as file:
            file.write(f'Пользователь {self.user["card"]} нажал кнопку "Другая сумма"\n')

    def button_VNESTI(self):
        self.VNESTI.clicked.connect(self.vnesti)

    def vnesti(self):
        self.VNESTI = VNESTI(self.user, self.data)
        self.VNESTI.show()
        self.close()
        with open("Логи.txt", 'a') as file:
            file.write(f'Пользователь {self.user["card"]} нажал кнопку "Внести"\n')

    def button_Balance(self):
        self.Balance.clicked.connect(self.open_balance)

    def open_balance(self):
        self.BALANCE = Balance(self.user, self.data)
        self.BALANCE.show()
        self.close()
        with open("Логи.txt", 'a') as file:
            file.write(f'Пользователь {self.user["card"]} нажал кнопку "Показать баланс"\n')

    def Snyatb_900(self):
        self.pushButton_900.clicked.connect(lambda: self.Snyatie_900())

    def Snyatie_900(self):
        with open("Кассета_1.txt", "r") as file:
            cas_5000 = int(file.readline())
        with open("Кассета_2.txt", "r") as file:
            cas_2000 = int(file.readline())
        with open("Кассета_3.txt", "r") as file:
            cas_1000 = int(file.readline())
        with open("Кассета_4.txt", "r") as file:
            cas_500 = int(file.readline())
        with open("Кассета_5.txt", "r") as file:
            cas_200 = int(file.readline())
        with open("Кассета_6.txt", "r") as file:
            cas_100 = int(file.readline())
        with open("Кассета_7.txt", "r") as file:
            cas_50 = int(file.readline())
        balance = self.user['balance']
        count = int(900)
        if balance>=count:
            Flag = True
            while count > 0:
                if count >= 5000 and cas_5000 > 0:
                    count = count - 5000
                    balance = balance - 5000
                    cas_5000 = cas_5000 - 1
                elif count >= 2000 and cas_2000 > 0:
                    count = count - 2000
                    balance = balance - 2000
                    cas_2000 = cas_2000 - 1
                elif count >= 1000 and cas_1000 > 0:
                    count = count - 1000
                    balance = balance - 1000
                    cas_1000 = cas_1000 - 1
                elif count >= 500 and cas_500 > 0:
                    count = count - 500
                    balance = balance - 500
                    cas_500 = cas_500 - 1
                elif count >= 200 and cas_200 > 0:
                    count = count - 200
                    balance = balance - 200
                    cas_200 = cas_200 - 1
                elif count >= 100 and cas_100 > 0:
                    count = count - 100
                    balance = balance - 100
                    cas_100 = cas_100 - 1
                elif count >= 50 and cas_50 > 0:
                    count = count - 50
                    balance = balance - 50
                    cas_50 = cas_50 - 1
                else:
                    Flag = False
                    error = QMessageBox()
                    error.setWindowTitle("Ошибка")
                    error.setText("Не хватает банкнот! Пожалуйста попробуйте снять другую сумму")
                    error.setIcon(QMessageBox.Warning)
                    error.setStandardButtons(QMessageBox.Ok)
                    error.exec_()

                    with open("Логи.txt", 'a') as file:
                        with open("Логи.txt", 'a') as file:
                            file.write(f"Пользователь {self.user['card']} попытался снять 900 рублей\n")
                    break
            if Flag:
                cas_5000 = str(cas_5000)
                cas_2000 = str(cas_2000)
                cas_1000 = str(cas_1000)
                cas_500 = str(cas_500)
                cas_200 = str(cas_200)
                cas_100 = str(cas_100)
                cas_50 = str(cas_50)

                with open("Кассета_1.txt", "w+") as file:
                    file.write(cas_5000)
                with open("Кассета_2.txt", "w+") as file:
                    file.write(cas_2000)
                with open("Кассета_3.txt", "w+") as file:
                    file.write(cas_1000)
                with open("Кассета_4.txt", "w+") as file:
                    file.write(cas_500)
                with open("Кассета_5.txt", "w+") as file:
                    file.write(cas_200)
                with open("Кассета_6.txt", "w+") as file:
                    file.write(cas_100)
                with open("Кассета_7.txt", "w+") as file:
                    file.write(cas_50)

                index = -1
                for i in range(len(self.data)):
                    if self.data[i]['password'] == self.user['password']:
                        index = i
                        break
                if index != -1:
                    self.data[index]['balance'] = balance
                json_object = json.dumps(self.data, indent=1)
                with open('Пользователи.json', 'w') as f:
                    f.write(json_object)
                Good = QMessageBox()
                Good.setWindowTitle("Успешно")
                Good.setText("Ваши деньги были успешно сняты")
                Good.setIcon(QMessageBox.Information)
                Good.setStandardButtons(QMessageBox.Ok)

                Good.exec_()
                with open("Логи.txt", 'a') as file:
                    file.write(f"Пользователь {self.user['card']} снял 900 рублей\n")
        else:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Не хватает денег на вашем балансе! Попробуйте ещё раз")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()
            with open("Логи.txt", 'a') as file:
                with open("Логи.txt", 'a') as file:
                    file.write(f"Пользователь {self.user['card']} попытался снять 900 рублей\n")

    def Snyatb_2500(self):
        self.pushButton_2500.clicked.connect(lambda: self.Snyatie_2500())

    def Snyatie_2500(self):
        with open("Кассета_1.txt", "r") as file:
            cas_5000 = int(file.readline())
        with open("Кассета_2.txt", "r") as file:
            cas_2000 = int(file.readline())
        with open("Кассета_3.txt", "r") as file:
            cas_1000 = int(file.readline())
        with open("Кассета_4.txt", "r") as file:
            cas_500 = int(file.readline())
        with open("Кассета_5.txt", "r") as file:
            cas_200 = int(file.readline())
        with open("Кассета_6.txt", "r") as file:
            cas_100 = int(file.readline())
        with open("Кассета_7.txt", "r") as file:
            cas_50 = int(file.readline())
        balance = self.user['balance']
        count = int(2500)
        if balance >= count:
            Flag = True
            while count > 0:
                if count >= 5000 and cas_5000 > 0:
                    count = count - 5000
                    balance = balance - 5000
                    cas_5000 = cas_5000 - 1
                elif count >= 2000 and cas_2000 > 0:
                    count = count - 2000
                    balance = balance - 2000
                    cas_2000 = cas_2000 - 1
                elif count >= 1000 and cas_1000 > 0:
                    count = count - 1000
                    balance = balance - 1000
                    cas_1000 = cas_1000 - 1
                elif count >= 500 and cas_500 > 0:
                    count = count - 500
                    balance = balance - 500
                    cas_500 = cas_500 - 1
                elif count >= 200 and cas_200 > 0:
                    count = count - 200
                    balance = balance - 200
                    cas_200 = cas_200 - 1
                elif count >= 100 and cas_100 > 0:
                    count = count - 100
                    balance = balance - 100
                    cas_100 = cas_100 - 1
                elif count >= 50 and cas_50 > 0:
                    count = count - 50
                    balance = balance - 50
                    cas_50 = cas_50 - 1
                else:
                    Flag = False
                    error = QMessageBox()
                    error.setWindowTitle("Ошибка")
                    error.setText("Не хватает банкнот! Пожалуйста попробуйте снять другую сумму")
                    error.setIcon(QMessageBox.Warning)
                    error.setStandardButtons(QMessageBox.Ok)
                    error.exec_()

                    with open("Логи.txt", 'a') as file:
                        file.write(f"Пользователь {self.user['card']} попытался снять 2500 рублей\n")
                    break
            if Flag:
                cas_5000 = str(cas_5000)
                cas_2000 = str(cas_2000)
                cas_1000 = str(cas_1000)
                cas_500 = str(cas_500)
                cas_200 = str(cas_200)
                cas_100 = str(cas_100)
                cas_50 = str(cas_50)

                with open("Кассета_1.txt", "w+") as file:
                    file.write(cas_5000)
                with open("Кассета_2.txt", "w+") as file:
                    file.write(cas_2000)
                with open("Кассета_3.txt", "w+") as file:
                    file.write(cas_1000)
                with open("Кассета_4.txt", "w+") as file:
                    file.write(cas_500)
                with open("Кассета_5.txt", "w+") as file:
                    file.write(cas_200)
                with open("Кассета_6.txt", "w+") as file:
                    file.write(cas_100)
                with open("Кассета_7.txt", "w+") as file:
                    file.write(cas_50)
                index = -1
                for i in range(len(self.data)):
                    if self.data[i]['password'] == self.user['password']:
                        index = i
                        break
                if index != -1:
                    self.data[index]['balance'] = balance
                json_object = json.dumps(self.data, indent=1)
                with open('Пользователи.json', 'w') as f:
                    f.write(json_object)
                Good = QMessageBox()
                Good.setWindowTitle("Успешно")
                Good.setText("Ваши деньги были успешно сняты")
                Good.setIcon(QMessageBox.Information)
                Good.setStandardButtons(QMessageBox.Ok)

                Good.exec_()
                with open("Логи.txt", 'a') as file:
                    file.write(f"Пользователь {self.user['card']} снял 2500 рублей\n")
        else:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Не хватает денег на вашем балансе! Попробуйте ещё раз")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()
            with open("Логи.txt", 'a') as file:
                file.write(f"Пользователь {self.user['card']} попытался снять 2500 рублей\n")

    def Snyatb_24400(self):
        self.pushButton_24400.clicked.connect(lambda: self.Snyatie_24400())

    def Snyatie_24400(self):
        with open("Кассета_1.txt", "r") as file:
            cas_5000 = int(file.readline())
        with open("Кассета_2.txt", "r") as file:
            cas_2000 = int(file.readline())
        with open("Кассета_3.txt", "r") as file:
            cas_1000 = int(file.readline())
        with open("Кассета_4.txt", "r") as file:
            cas_500 = int(file.readline())
        with open("Кассета_5.txt", "r") as file:
            cas_200 = int(file.readline())
        with open("Кассета_6.txt", "r") as file:
            cas_100 = int(file.readline())
        with open("Кассета_7.txt", "r") as file:
            cas_50 = int(file.readline())
        balance = self.user['balance']
        count = int(24400)
        if balance >= count:
            Flag = True
            while count > 0:
                if count >= 5000 and cas_5000 > 0:
                    count = count - 5000
                    balance = balance - 5000
                    cas_5000 = cas_5000 - 1
                elif count >= 2000 and cas_2000 > 0:
                    count = count - 2000
                    balance = balance - 2000
                    cas_2000 = cas_2000 - 1
                elif count >= 1000 and cas_1000 > 0:
                    count = count - 1000
                    balance = balance - 1000
                    cas_1000 = cas_1000 - 1
                elif count >= 500 and cas_500 > 0:
                    count = count - 500
                    balance = balance - 500
                    cas_500 = cas_500 - 1
                elif count >= 200 and cas_200 > 0:
                    count = count - 200
                    balance = balance - 200
                    cas_200 = cas_200 - 1
                elif count >= 100 and cas_100 > 0:
                    count = count - 100
                    balance = balance - 100
                    cas_100 = cas_100 - 1
                elif count >= 50 and cas_50 > 0:
                    count = count - 50
                    balance = balance - 50
                    cas_50 = cas_50 - 1
                else:
                    Flag = False
                    error = QMessageBox()
                    error.setWindowTitle("Ошибка")
                    error.setText("Не хватает банкнот! Пожалуйста попробуйте снять другую сумму")
                    error.setIcon(QMessageBox.Warning)
                    error.setStandardButtons(QMessageBox.Ok)
                    error.exec_()

                    with open("Логи.txt", 'a') as file:
                        file.write(f"Пользователь {self.user['card']} попытался снять 24400 рублей\n")
                    break
            if Flag:
                cas_5000 = str(cas_5000)
                cas_2000 = str(cas_2000)
                cas_1000 = str(cas_1000)
                cas_500 = str(cas_500)
                cas_200 = str(cas_200)
                cas_100 = str(cas_100)
                cas_50 = str(cas_50)

                with open("Кассета_1.txt", "w+") as file:
                    file.write(cas_5000)
                with open("Кассета_2.txt", "w+") as file:
                    file.write(cas_2000)
                with open("Кассета_3.txt", "w+") as file:
                    file.write(cas_1000)
                with open("Кассета_4.txt", "w+") as file:
                    file.write(cas_500)
                with open("Кассета_5.txt", "w+") as file:
                    file.write(cas_200)
                with open("Кассета_6.txt", "w+") as file:
                    file.write(cas_100)
                with open("Кассета_7.txt", "w+") as file:
                    file.write(cas_50)

                index = -1
                for i in range(len(self.data)):
                    if self.data[i]['password'] == self.user['password']:
                        index = i
                        break
                if index != -1:
                    self.data[index]['balance'] = balance
                json_object = json.dumps(self.data, indent=1)
                with open('Пользователи.json', 'w') as f:
                    f.write(json_object)
                Good = QMessageBox()
                Good.setWindowTitle("Успешно")
                Good.setText("Ваши деньги были успешно сняты")
                Good.setIcon(QMessageBox.Information)
                Good.setStandardButtons(QMessageBox.Ok)

                Good.exec_()
                with open("Логи.txt", 'a') as file:
                    file.write(f"Пользователь {self.user['card']} снял 24400 рублей\n")
        else:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Не хватает денег на вашем балансе! Попробуйте ещё раз")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()
            with open("Логи.txt", 'a') as file:
                file.write(f"Пользователь {self.user['card']} попытался снять 24400 рублей\n")


class PINcode(QtWidgets.QMainWindow):
    pinpass = ''
    def __init__(self, data):
        super(PINcode, self).__init__()
        self.setObjectName("NieRBank")
        self.resize(453, 630)
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.Main_label = QtWidgets.QLabel(self.centralwidget)
        self.Main_label.setGeometry(QtCore.QRect(0, 0, 453, 630))
        self.Main_label.setText("")
        self.Main_label.setPixmap(QtGui.QPixmap("Menu.png"))
        self.Main_label.setObjectName("Main_label")
        self.label_back = QtWidgets.QLabel(self.centralwidget)
        self.label_back.setGeometry(QtCore.QRect(340, 10, 102, 42))
        self.label_back.setText("")
        self.label_back.setPixmap(QtGui.QPixmap("Buttons.png"))
        self.label_back.setObjectName("label_back")
        self.BACK_button = QtWidgets.QPushButton(self.centralwidget)
        self.BACK_button.setGeometry(QtCore.QRect(340, 10, 102, 40))
        self.BACK_button.setText("Назад")
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.BACK_button.setFont(font)
        self.BACK_button.setStyleSheet("color: rgb(0, 0, 0);\n"
"border: none;")
        self.BACK_button.setObjectName("BACK_button")
        self.label_PIN = QtWidgets.QLabel(self.centralwidget)
        self.label_PIN.setGeometry(QtCore.QRect(138, 190, 251, 28))
        self.label_PIN.setText("Введите ПИН-код")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_PIN.setFont(font)
        self.label_PIN.setStyleSheet("color: rgb(0, 0, 0);\n"
"border: none;")
        self.label_PIN.setObjectName("label_PIN")
        self.butn1 = QtWidgets.QPushButton(self.centralwidget)
        self.butn1.setGeometry(QtCore.QRect(30, 370, 130, 61))
        self.butn1.setText("1")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.butn1.setFont(font)
        self.butn1.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.butn1.setObjectName("butn1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 360, 435, 261))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Buttons.png"))
        self.label_2.setObjectName("label_2")
        self.butn2 = QtWidgets.QPushButton(self.centralwidget)
        self.butn2.setGeometry(QtCore.QRect(160, 370, 130, 61))
        self.butn2.setText("2")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.butn2.setFont(font)
        self.butn2.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.butn2.setObjectName("butn2")
        self.butn3 = QtWidgets.QPushButton(self.centralwidget)
        self.butn3.setGeometry(QtCore.QRect(290, 370, 130, 61))
        self.butn3.setText("3")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.butn3.setFont(font)
        self.butn3.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.butn3.setObjectName("butn3")
        self.butn4 = QtWidgets.QPushButton(self.centralwidget)
        self.butn4.setGeometry(QtCore.QRect(30, 431, 130, 61))
        self.butn4.setText("4")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.butn4.setFont(font)
        self.butn4.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.butn4.setObjectName("butn4")
        self.butn7 = QtWidgets.QPushButton(self.centralwidget)
        self.butn7.setGeometry(QtCore.QRect(30, 491, 130, 61))
        self.butn7.setText("7")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.butn7.setFont(font)
        self.butn7.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.butn7.setObjectName("butn7")
        self.butn5 = QtWidgets.QPushButton(self.centralwidget)
        self.butn5.setGeometry(QtCore.QRect(160, 431, 130, 61))
        self.butn5.setText("5")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.butn5.setFont(font)
        self.butn5.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.butn5.setObjectName("butn5")
        self.butn6 = QtWidgets.QPushButton(self.centralwidget)
        self.butn6.setGeometry(QtCore.QRect(290, 431, 130, 61))
        self.butn6.setText("6")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.butn6.setFont(font)
        self.butn6.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.butn6.setObjectName("butn6")
        self.butn8 = QtWidgets.QPushButton(self.centralwidget)
        self.butn8.setGeometry(QtCore.QRect(160, 491, 130, 61))
        self.butn8.setText("8")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.butn8.setFont(font)
        self.butn8.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.butn8.setObjectName("butn8")
        self.butn9 = QtWidgets.QPushButton(self.centralwidget)
        self.butn9.setGeometry(QtCore.QRect(290, 491, 130, 61))
        self.butn9.setText("9")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.butn9.setFont(font)
        self.butn9.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.butn9.setObjectName("butn9")
        self.butn0 = QtWidgets.QPushButton(self.centralwidget)
        self.butn0.setGeometry(QtCore.QRect(160, 551, 130, 61))
        self.butn0.setText("0")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.butn0.setFont(font)
        self.butn0.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.butn0.setObjectName("butn0")
        self.label_pin_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_pin_1.setGeometry(QtCore.QRect(120, 220, 41, 61))
        self.label_pin_1.setText("_")
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_pin_1.setFont(font)
        self.label_pin_1.setStyleSheet("background-color: rgb(108, 108, 108);")
        self.label_pin_1.setObjectName("label_pin_1")
        self.label_pin_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_pin_2.setGeometry(QtCore.QRect(175, 220, 41, 61))
        self.label_pin_2.setText("_")
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_pin_2.setFont(font)
        self.label_pin_2.setStyleSheet("background-color: rgb(108, 108, 108);")
        self.label_pin_2.setObjectName("label_pin_2")
        self.label_pin_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_pin_3.setGeometry(QtCore.QRect(231, 220, 41, 61))
        self.label_pin_3.setText("_")
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_pin_3.setFont(font)
        self.label_pin_3.setStyleSheet("background-color: rgb(108, 108, 108);")
        self.label_pin_3.setObjectName("label_pin_3")
        self.label_pin_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_pin_4.setGeometry(QtCore.QRect(287, 220, 41, 61))
        self.label_pin_4.setText("_")
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_pin_4.setFont(font)
        self.label_pin_4.setStyleSheet("background-color: rgb(108, 108, 108);")
        self.label_pin_4.setObjectName("label_pin_4")
        self.Main_label.raise_()
        self.label_back.raise_()
        self.BACK_button.raise_()
        self.label_PIN.raise_()
        self.label_2.raise_()
        self.butn1.raise_()
        self.butn2.raise_()
        self.butn3.raise_()
        self.butn4.raise_()
        self.butn5.raise_()
        self.butn6.raise_()
        self.butn7.raise_()
        self.butn8.raise_()
        self.butn9.raise_()
        self.butn0.raise_()
        self.label_pin_1.raise_()
        self.label_pin_2.raise_()
        self.label_pin_3.raise_()
        self.label_pin_4.raise_()
        self.setCentralWidget(self.centralwidget)
        self.data = data

        self.numbers()
        self.pushbutton_back()
        QtCore.QMetaObject.connectSlotsByName(self)

    def pushbutton_back(self):
        self.BACK_button.clicked.connect(self.back)

    def back(self):
        self.BeginWindow = Begin_Window(self.data)
        self.BeginWindow.show()
        self.close()
        with open("Логи.txt", 'a') as file:
            file.write('Пользователь вернулся к первому окну' + '\n')

    def numbers(self):
        self.butn0.clicked.connect(lambda: self.write_number(self.butn0.text()))
        self.butn1.clicked.connect(lambda: self.write_number(self.butn1.text()))
        self.butn2.clicked.connect(lambda: self.write_number(self.butn2.text()))
        self.butn3.clicked.connect(lambda: self.write_number(self.butn3.text()))
        self.butn4.clicked.connect(lambda: self.write_number(self.butn4.text()))
        self.butn5.clicked.connect(lambda: self.write_number(self.butn5.text()))
        self.butn6.clicked.connect(lambda: self.write_number(self.butn6.text()))
        self.butn7.clicked.connect(lambda: self.write_number(self.butn7.text()))
        self.butn8.clicked.connect(lambda: self.write_number(self.butn8.text()))
        self.butn9.clicked.connect(lambda: self.write_number(self.butn9.text()))

    def write_number(self, number):
            Flag = True
            if self.label_pin_1.text() == "_" and Flag:
                self.label_pin_1.setText("*")
                Flag = False
            if self.label_pin_2.text() == "_" and Flag:
                self.label_pin_2.setText("*")
                Flag = False
            if self.label_pin_3.text() == "_" and Flag:
                self.label_pin_3.setText("*")
                Flag = False
            if self.label_pin_4.text() == "_" and Flag:
                self.label_pin_4.setText("*")
            self.pinpass += str(number)
            if Flag:
                user = None
                Flag1 = True
                for dataUser in self.data:
                    if dataUser['password'] == self.pinpass:
                        user = dataUser
                        Flag1 = False
                        with open("Логи.txt", 'a') as file:
                            file.write('Пользователь ввёл ПИН-код' + '\n')
                        break
                if Flag1:
                    user = self.New_user()
                self.Main_menu = Main_Menu(user, self.data)
                self.Main_menu.show()
                self.close()

    def New_user(self):
        c = ''
        for i in range(4):
            c += str(random.randint(0, 9))
        user = {
            "password" : self.pinpass,
            "card" : '****' + c,
            "balance" : 0
        }
        self.data.append(user)
        json_object = json.dumps(data, indent=1)
        with open('Пользователи.json', 'w') as f:
            f.write(json_object)
        return user


class Begin_Window(QtWidgets.QMainWindow):
    def __init__(self, data):
        super(Begin_Window, self).__init__()
        self.setWindowTitle("NieRBank")
        self.setFixedSize(453, 630)
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 461, 741))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Main menu.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 210, 150, 151))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Proba2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(300, 300))
        self.pushButton.setAutoDefault(True)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 380, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setText("Начать")
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.setCentralWidget(self.centralwidget)
        self.data = data

        self.pushbutton_clicked()
        QtCore.QMetaObject.connectSlotsByName(self)

    def pushbutton_clicked(self):
        self.pushButton.clicked.connect(self.close_open)

    def close_open(self):
        self.PinCode = PINcode(self.data)
        self.PinCode.show()
        self.close()
        with open("Логи.txt", 'a') as file:
            file.write('Пользователь приложил карту' + '\n')


if __name__ == "__main__":
    import sys
    data = J1()
    app = QApplication(sys.argv)
    w = Begin_Window(data)
    w.show()
    sys.exit(app.exec_())