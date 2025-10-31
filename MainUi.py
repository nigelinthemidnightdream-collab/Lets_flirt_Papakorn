import sys
from PySide6 import QtCore, QtGui, QtWidgets
from shiboken6 import wrapInstance
import maya.OpenMayaUI as omui

sys.path.append(r'C:/Users/jajap/OneDrive/Documents/maya/2026/scripts/Lets_flirt_Papakorn')
from LowPolyUtil import LowPolyDialog
from ReverseFacenTposeUtil import ReverseFaceNTposeDialog
from BrokenTextureUtil import BrokenTexturesDialog
from SecretUtil import SecretDialog

ROOT_RESOURCE_DIR = 'C:/Users/jajap/OneDrive/Documents/maya/2026/scripts'


class LetsFlirtDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("🤓 Let's go flirt with Papakorn")
        self.resize(1180, 650)
        self.setStyleSheet('background-color: #6095FE')

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setAlignment(QtCore.Qt.AlignCenter)
        self.setLayout(self.mainLayout)

        self.imageLabel = QtWidgets.QLabel()
        self.imagePixmap = QtGui.QPixmap(f'{ROOT_RESOURCE_DIR}/Lets_flirt_Papakorn/images/Title_Papakorn.png')
        scaled_pixmap = self.imagePixmap.scaled(
            QtCore.QSize(800, 250),
            QtCore.Qt.KeepAspectRatio,
            QtCore.Qt.SmoothTransformation
        )
        self.imageLabel.setPixmap(scaled_pixmap)
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainLayout.addWidget(self.imageLabel)

        button_style = '''
            QPushButton {
                background-color: #F2F2EB;
                color: #275AF2;
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
        self.lowPolyButton.clicked.connect(self.openLowPoly)

        self.tposeButton = QtWidgets.QPushButton('Reverse face & T-pose')
        self.tposeButton.setStyleSheet(button_style)
        self.tposeButton.clicked.connect(self.openReversenTpose)

        self.brokenButton = QtWidgets.QPushButton('Broken Textures')
        self.brokenButton.setStyleSheet(button_style)
        self.brokenButton.clicked.connect(self.openBrokenTexture)

        self.secretButton = QtWidgets.QPushButton('💙 Secret Route 💙')
        self.secretButton.setStyleSheet(button_style)
        self.secretButton.clicked.connect(self.openSecretRoute)
        self.secretButton.hide()

        self.buttonLayout.addWidget(self.lowPolyButton)
        self.buttonLayout.addWidget(self.tposeButton)
        self.buttonLayout.addWidget(self.brokenButton)
        self.buttonLayout.addWidget(self.secretButton)
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

        self.lowPolyPopup = None
        self.reversePopup = None
        self.brokenPopup = None
        self.secretPopup = None

        self.routes_completed = {
            "lowpoly": False,
            "reverse": False,
            "broken": False
        }

    def openLowPoly(self):
        if not self.lowPolyPopup:
            self.lowPolyPopup = LowPolyDialog(self)
            self.lowPolyPopup.finished.connect(lambda: self.markRouteCompleted("lowpoly"))
        self.lowPolyPopup.show()
        self.lowPolyPopup.raise_()

    def openReversenTpose(self):
        if not self.reversePopup:
            self.reversePopup = ReverseFaceNTposeDialog(self)
            self.reversePopup.finished.connect(lambda: self.markRouteCompleted("reverse"))
        self.reversePopup.show()
        self.reversePopup.raise_()

    def openBrokenTexture(self):
        if not self.brokenPopup:
            self.brokenPopup = BrokenTexturesDialog(self)
            self.brokenPopup.finished.connect(lambda: self.markRouteCompleted("broken"))
        self.brokenPopup.show()
        self.brokenPopup.raise_()

    def markRouteCompleted(self, route_name):
        self.routes_completed[route_name] = True

        if all(self.routes_completed.values()):
            self.unlockSecretRoute()

    def unlockSecretRoute(self):
        self.secretButton.show()
        self.secretButton.setText('💙 Secret Route Unlocked! 💙')

    def openSecretRoute(self):
        if not self.secretPopup:
            self.secretPopup = SecretDialog(self)
        self.secretPopup.show()
        self.secretPopup.raise_()

def run():
    global ui
    try:
        ui.close()
    except:
        pass

    ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
    ui = LetsFlirtDialog(parent=ptr)
    ui.show()