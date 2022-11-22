from random import randint
import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPainter, QPen
from PyQt5.QtWidgets import (
    QApplication, QWidget,
)

from main_window import Ui_Form


class CircleGenerator(QWidget, Ui_Form):
    SCREEN_SIZE = (500, 500)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.center = (250, 250)
        self.setGeometry(300, 300, *CircleGenerator.SCREEN_SIZE)
        self.setWindowTitle('Git и желтые окружности')
        self.do_paint = False
        self.gen_circle_btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()
        self.do_paint = False

    def generate_rand_color(self):
        return tuple(randint(0, 255) for _ in range(3))

    def generate_rand_diametr(self):
        return randint(100, 255)

    def draw_flag(self, qp):
        pen = QPen(QColor(*self.generate_rand_color()), 9)
        qp.setPen(pen)
        diametr = self.generate_rand_diametr()
        qp.drawEllipse(150, 150, diametr, diametr)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    circle_gen = CircleGenerator()
    circle_gen.show()
    sys.exit(app.exec())
