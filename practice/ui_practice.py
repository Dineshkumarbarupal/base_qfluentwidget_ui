from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel

class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Button for WhatsApp Automation
        self.whatsapp_button = QPushButton("Click here to automate WhatsApp")
        self.whatsapp_button.clicked.connect(self.open_whatsapp_interface)

        layout.addWidget(QLabel("Automation"))
        layout.addWidget(self.whatsapp_button)

        self.setLayout(layout)

    def open_whatsapp_interface(self):
        # Signal to open WhatsApp interface
        self.parentWidget().open_whatsapp_interface()


class WhatsAppInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Welcome to WhatsApp Automation"))
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Automation-Base-Software")

        # Create Home Page and WhatsApp Interface
        self.home_page = HomePage()
        self.whatsapp_interface = WhatsAppInterface()

        # Set Home Page as central widget
        self.setCentralWidget(self.home_page)

    def open_whatsapp_interface(self):
        # Replace current widget with WhatsApp interface
        self.setCentralWidget(self.whatsapp_interface)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
