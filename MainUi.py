from PySide6 import QtCore, QtGui, QtWidgets
from shiboken6 import wrapInstance
import maya.OpenMayaUI as omui

ROOT_RESOURCE_DIR = 'C:/Users/jajap/OneDrive/Documents/maya/2026/scripts'

class LetsFlirtDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("🤓 Let's go flirt with Papakorn")
        self.resize(1280, 720)
        self.setStyleSheet('background-color: #6095FE;')

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setAlignment(QtCore.Qt.AlignCenter)
        self.setLayout(self.mainLayout)

        self.imageLabel = QtWidgets.QLabel()
        self.imagePixmap = QtGui.QPixmap(f"{ROOT_RESOURCE_DIR}/Lets_flirt_Papakorn/Title_Papakorn.png")
        scaled_pixmap = self.imagePixmap.scaled(
            QtCore.QSize(720, 250),
            QtCore.Qt.KeepAspectRatio,
            QtCore.Qt.SmoothTransformation
        )
        self.imageLabel.setPixmap(scaled_pixmap)
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainLayout.addWidget(self.imageLabel)

        button_style = '''
            QPushButton {
                background-color: #F2F2EB;
                color: blue;
                border-radius: 8px;
                font-size: 26px;
                font-family: Candara;
                font-weight: bold;
                padding: 10px 20px;
                min-width: 300px;
            }
            QPushButton:hover {
                background-color: #9BC1F2;
            }
            QPushButton:pressed {
                background-color: #275AF2;
                color: white;
            }
        '''

        self.buttonLayout = QtWidgets.QVBoxLayout()
        self.buttonLayout.setAlignment(QtCore.Qt.AlignCenter)
        self.buttonLayout.setSpacing(20)

        self.lowPolyButton = QtWidgets.QPushButton('Low Poly')
        self.lowPolyButton.setStyleSheet(button_style)

        self.tposeButton = QtWidgets.QPushButton('T-pose + Reverse face')
        self.tposeButton.setStyleSheet(button_style)

        self.brokenButton = QtWidgets.QPushButton('Broken Textures')
        self.brokenButton.setStyleSheet(button_style)

        self.buttonLayout.addWidget(self.lowPolyButton)
        self.buttonLayout.addWidget(self.tposeButton)
        self.buttonLayout.addWidget(self.brokenButton)
        self.mainLayout.addLayout(self.buttonLayout)

        self.exitButton = QtWidgets.QPushButton('exit')
        self.exitButton.setFixedSize(100, 40)
        self.exitButton.setStyleSheet('''
            QPushButton {
                background-color: white;
                color: #275AF2;
                border: none;
                border-radius: 6px;
                font-family: Candara;
                font-size: 18px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #EAF0FF;
            }
            QPushButton:pressed {
                background-color: #275AF2;
                color: white;
            }
        ''')
        self.exitButton.clicked.connect(self.close)

        bottomLayout = QtWidgets.QHBoxLayout()
        bottomLayout.addStretch()
        bottomLayout.addWidget(self.exitButton)
        self.mainLayout.addLayout(bottomLayout)

def run():
    global ui
    try:
        ui.close()
    except:
        pass

    ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
    ui = LetsFlirtDialog(parent=ptr)
    ui.show()
