from PySide6 import QtCore, QtGui, QtWidgets

ROOT_RESOURCE_DIR = r"C:/Users/jajap/OneDrive/Documents/maya/2026/scripts"

class LowPolyDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("🤓 Low Poly Route")
        self.resize(890, 650)
        self.setStyleSheet('background-color: #6095FE')

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setAlignment(QtCore.Qt.AlignCenter)
        self.setLayout(self.mainLayout)

        self.imageLabel = QtWidgets.QLabel()
        self.imagePixmap = QtGui.QPixmap(f"{ROOT_RESOURCE_DIR}/Lets_flirt_Papakorn/images/Low_Poly.png""")
        scaled_pixmap = self.imagePixmap.scaled(
            QtCore.QSize(1060, 608),
            QtCore.Qt.KeepAspectRatio,
            QtCore.Qt.SmoothTransformation
        )
        self.imageLabel.setPixmap(scaled_pixmap)
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainLayout.addWidget(self.imageLabel)

        textLabel = QtWidgets.QLabel("ฉันตัวเหลี่ยม\nชอบม้า ชอบม้า?")
        textLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        textLabel.setWordWrap(True)
        textLabel.setStyleSheet("font-size: 18px; font-family: Candara;")
        self.mainLayout.addWidget(textLabel)
