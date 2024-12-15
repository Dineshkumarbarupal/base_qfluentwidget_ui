# coding:utf-8
import sys

from PyQt5.QtCore import Qt, QUrl,QSize
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtWidgets import QApplication, QFrame, QHBoxLayout,QVBoxLayout,QSizePolicy,QLabel,QSpacerItem
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, Theme, FluentWindow,
                            NavigationAvatarWidget, qrouter, SubtitleLabel, setFont, InfoBadge,
                            InfoBadgePosition, FluentBackgroundTheme, PrimaryPushButton,LineEdit, BodyLabel)
from qfluentwidgets import FluentIcon as FIF
from whatsapp_automate import WaAutomate


class Widget(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = SubtitleLabel(text, self)
        self.hBoxLayout = QVBoxLayout(self)

        setFont(self.label, 24)
        self.label.setAlignment(Qt.AlignCenter)
        self.hBoxLayout.addWidget(self.label,alignment= Qt.AlignCenter)
        self.setObjectName(text.replace(' ', '-'))

    


class Window(FluentWindow):

    def __init__(self):
        super().__init__()

        # create sub interface
        self.homeInterface = Widget('Home Interface', self)
        self.whatsappInterface = Widget('Whatsapp Automation', self)
        self.amazonInterface = Widget('Amazon Automation', self)
        self.telegramInterface = Widget('Telegram Interface', self)
        self.youtubeInterface = Widget('Youtube Interface', self)
        self.settingInterface = Widget('Setting Interface', self)
        self.instaInterface = Widget('Insta Interface', self)
        self.instaInterface1 = Widget('Insta Interface 1', self)
        self.instaInterface2 = Widget('Insta Interface 2', self)
        self.instaInterface1_1 = Widget('Insta Interface 1-1', self)

        self.whatsappInterface.label.setText('')
        
        self.addFrameToWhatsAppInterface()
        self.initNavigation()
        self.initWindow()

    
    def addFrameToWhatsAppInterface(self):
        """Add a frame inside the WhatsApp interface."""
        # Create a layout for WhatsApp interface
        layout = QVBoxLayout(self.whatsappInterface)

        # Create a frame
        frame = QFrame(self.whatsappInterface)
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        frame.setStyleSheet("background-color: white; border-radius: 10px")
        frame.setFixedSize(200,200)

        # Add content to the frame (e.g., a label)
        frame_layout = QVBoxLayout(frame)
        label = QLabel("This is a frame inside WhatsApp Interface", frame)
        label.setAlignment(Qt.AlignCenter)
        frame_layout.addWidget(label)

        # Add the frame to the WhatsApp interface layout
        start_button = PrimaryPushButton("start")
        frame_layout.addWidget(start_button,alignment= Qt.AlignCenter)
        layout.addWidget(frame,alignment=Qt.AlignCenter)

    def initNavigation(self):

        insta_logo = QIcon("logos/insta.png")
        telegram_logo = QIcon("logos/telegram.png")
        whatsapp_icon = QIcon("logos/whatsapp_logo.png")
        amazon_logo = QIcon("logos/amazon_logo.png")
        youtube_logo = QIcon("logos/youtube_PNG102347.png")


        self.addSubInterface(self.telegramInterface, telegram_logo, 'Telegram Automation', NavigationItemPosition.SCROLL)
        self.navigationInterface.addSeparator()
        self.addSubInterface(self.homeInterface, FIF.HOME, 'Home')
        self.navigationInterface.addSeparator()
        self.addSubInterface(self.whatsappInterface, whatsapp_icon, 'WhatsApp Automation')
        self.navigationInterface.addSeparator()
        self.addSubInterface(self.amazonInterface, amazon_logo, 'Amazon Automation')
        self.navigationInterface.addSeparator()
        self.addSubInterface(self.youtubeInterface, youtube_logo, 'Youtube Automation')
        self.navigationInterface.addSeparator()
        self.addSubInterface(self.instaInterface, insta_logo, 'Instagram Automatin', NavigationItemPosition.SCROLL)
        self.addSubInterface(self.instaInterface1, FIF.ALBUM, 'insta 1', parent=self.instaInterface)
        self.addSubInterface(self.instaInterface1_1, FIF.ALBUM, 'insta 1.1', parent=self.instaInterface1)
        self.addSubInterface(self.instaInterface2, FIF.ALBUM, 'insta 2', parent=self.instaInterface)


        # add custom widget to bottom
        self.navigationInterface.addWidget(
            routeKey='avatar',
            widget=NavigationAvatarWidget('Alien', 'resource/shoko.png'),
            onClick=self.showMessageBox,
            position=NavigationItemPosition.BOTTOM,
        )

        self.addSubInterface(self.settingInterface, FIF.SETTING, 'Settings', NavigationItemPosition.BOTTOM)

        # self.contacts = LineEdit()
        # # Set placeholder text
        # self.contacts.setPlaceholderText("Enter contact name")
        # # Set text
        # # lineEdit.setText("shokokawaii@foxmail.com")
        # print(self.contacts.text())
        # # Enable clear button
        # self.contacts.setClearButtonEnabled(True)

        # self.contact_label = BodyLabel("Enter your contact detail")
        # self.massage_label = BodyLabel("Enter your massage")
        # self.massage = LineEdit()
        # self.massage.setPlaceholderText("Enter your massage")
        # # print(self.massage)
        
     
       
        # start_button = PrimaryPushButton("start",self.whatsappInterface)
        # start_button.clicked.connect(self.whatsapp_automate)
        # start_button.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)
        # start_button.setFixedSize(77,28)


        # self.whatsappInterface.hBoxLayout.setContentsMargins(0,300 , 0, 300)
       
        # self.whatsappInterface.hBoxLayout.addWidget(self.contact_label,alignment= Qt.AlignCenter)
        # self.whatsappInterface.hBoxLayout.addWidget(self.contacts, alignment= Qt.AlignCenter)
        # self.whatsappInterface.hBoxLayout.addWidget(self.massage_label,alignment= Qt.AlignCenter)
        # self.whatsappInterface.hBoxLayout.addWidget(self.massage, alignment=Qt.AlignCenter)
        # # self.whatsappInterface.hBoxLayout.setSpacing(1)
        # self.whatsappInterface.hBoxLayout.addWidget(start_button,alignment= Qt.AlignCenter)


        # add badge to navigation item
        # item = self.navigationInterface.widget(self.videoInterface.objectName())
        # InfoBadge.attension(
        #     text=9,
        #     parent=item.parent(),
        #     target=item,
        #     position=InfoBadgePosition.NAVIGATION_ITEM
        # )

        # NOTE: enable acrylic effect
        # self.navigationInterface.setAcrylicEnabled(True)

    def initWindow(self):
        self.resize(900, 700)
        self.setWindowIcon(QIcon('logos/base_software_logo.png'))
        self.setWindowTitle('Automation-Base-Software')

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)

        # set the minimum window width that allows the navigation panel to be expanded
        # self.navigationInterface.setMinimumExpandWidth(900)
        # self.navigationInterface.expand(useAni=False)

    def showMessageBox(self):
        w = MessageBox(
            'Source code',
            'There is the source code of this base software',
            self
        )
        w.yesButton.setText('Source code')
        w.cancelButton.setText('Skip')

        if w.exec():
            QDesktopServices.openUrl(QUrl("https://github.com/Dineshkumarbarupal/base_qfluentwidget_ui"))

    
    def whatsapp_automate(self):
        user_contect_input = self.contacts.text()
        user_massage = self.massage.text()
        
        if user_contect_input:

            WaAutomate(user_contect_input,user_massage)
        else:
            print("Enter valid input")


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    # setTheme(Theme.DARK)

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec_()