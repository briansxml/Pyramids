import random
import sys

from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)
        self.setFixedSize(800, 600)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        size1 = random.randint(20, 100)
        size2 = random.randint(20, 100)
        size3 = random.randint(20, 100)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(random.randint(0, self.width()),
                    random.randint(0, self.height()), size1,
                    size1)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(random.randint(0, self.width()),
                    random.randint(0, self.height()), size2,
                    size2)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(random.randint(0, self.width()),
                    random.randint(0, self.height()), size3,
                    size3)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
