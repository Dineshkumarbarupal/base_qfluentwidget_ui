import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtCore import  QEasingCurve
from qfluentwidgets import SmoothScrollArea,ImageLabel,SingleDirectionScrollArea

class Demo(SmoothScrollArea):

    def __init__(self):
        super().__init__()
        # Load a high-resolution image
        self.label = ImageLabel("6201771.jpg")

        # Custom smooth scrolling animation
        self.setScrollAnimation(Qt.Vertical, 400, QEasingCurve.OutQuint)
        self.setScrollAnimation(Qt.Horizontal, 400, QEasingCurve.OutQuint)

        # Scroll to a specific area
        self.horizontalScrollBar().setValue(1900)

        self.setWidget(self.label)
        self.resize(1200, 800)

        # scrollArea = SingleDirectionScrollArea(orient=Qt.Vertical)
        # scrollArea.resize(200, 400)

        # # There are many components in the vertical direction
        # view = QWidget()
        # layout = QVBoxLayout(view)
        # for i in range(1, 100):
        #     layout.addWidget(QPushButton(f"Button {i}"))

        # scrollArea.setWidget(view)



if __name__=='__main__':
    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    app.exec_()
