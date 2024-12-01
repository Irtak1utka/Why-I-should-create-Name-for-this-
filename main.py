from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QColor, QPainter
import sys
from PyQt6 import uic
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.flag = False
        self.Draw.clicked.connect(self.start)

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        a = randint(0, 250)
        qp.drawEllipse(100, 100, a, a)
        self.flag = False

    def start(self):
        self.flag = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())