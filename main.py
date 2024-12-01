from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox, QPushButton, QLabel, QTableWidget, QTableWidgetItem
import sys
from PyQt6 import uic
import sqlite3


def bobr(ar):
    con = sqlite3.connect("coffee.sqlite3")
    cur = con.cursor()
    res = cur.execute(f"""SELECT * FROM coffee
    WHERE sort_title = '{ar}'""").fetchall()[0]
    return res


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUa()

    def initUa(self):
        uic.loadUi('main.ui', self)
        self.resize(717, 300)
        con = sqlite3.connect("coffee.sqlite3")
        cur = con.cursor()
        res = cur.execute("""SELECT sort_title FROM coffee""").fetchall()
        for el in res:
            self.comboBox: QComboBox
            self.comboBox.addItem(el[0])
        self.but: QPushButton
        self.but.clicked.connect(self.hi)
        con.commit()
        cur.close()
        con.close()

    def hi(self):
        self.comboBox: QComboBox
        self.table = QTableWidget(2, 7, self)
        curva = bobr(self.comboBox.currentText())
        f = []
        ht = ["ID", "название сорта", "степень обжарки", "молотый/в зернах", "описание вкуса", "цена", "объем упаковки"]
        for i in range(len(ht)):
            self.table.setItem(0, i, QTableWidgetItem(ht[i]))
        self.table.resize(717, 90)
        self.table.show()
        for i in range(len(curva)):
            if curva[i] == 0 and i != 0:
                self.table.setItem(1, i, QTableWidgetItem("молотый"))
                f.append("молотый")
            elif curva[i] == 1 and i != 0:
                self.table.setItem(1, i, QTableWidgetItem("в зернах"))
                f.append("в зернах")
            else:
                self.table.setItem(1, i, QTableWidgetItem(str(curva[i])))
                f.append(str(curva[i]))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
