from PySide6 import QtCore, QtGui, QtWidgets
import sys

ROOT_RESOURCE_DIR = r"C:/Users/jajap/OneDrive/Documents/maya/2026/scripts"

class LowPolyDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("🤓 Low Poly Route")
        self.resize(890, 650)
        self.setStyleSheet("background-color: #6095FE;")

        # =============== MAIN LAYOUT ===================
        self.mainLayout = QtWidgets.QVBoxLayout(self)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(0)

        # ---------------- IMAGE (CHARACTER) ----------------
        self.imageLabel = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap(f"{ROOT_RESOURCE_DIR}/Lets_flirt_Papakorn/images/Low_Poly.png")
        scaled_pixmap = pixmap.scaled(
            QtCore.QSize(890, 500),
            QtCore.Qt.KeepAspectRatio,
            QtCore.Qt.SmoothTransformation
        )
        self.imageLabel.setPixmap(scaled_pixmap)
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setStyleSheet("background-color: transparent;")
        self.mainLayout.addWidget(self.imageLabel, stretch=4)

        self.choiceWidget = QtWidgets.QWidget()
        self.choiceLayout = QtWidgets.QVBoxLayout(self.choiceWidget)
        self.choiceLayout.setAlignment(QtCore.Qt.AlignCenter)
        self.choiceLayout.setSpacing(15)

        self.choiceWidget.setStyleSheet("background: transparent;")

        self.choice1 = self.createChoiceButton("ลองกด 3 ให้สมูทสิ ช่วยได้นะ", correct=True)
        self.choice2 = self.createChoiceButton("ฉันว่าแบบนี้นายก็เท่ดีออก", correct=False)

        self.choiceLayout.addWidget(self.choice1)
        self.choiceLayout.addWidget(self.choice2)
        self.mainLayout.addWidget(self.choiceWidget, alignment=QtCore.Qt.AlignCenter)
        self.choiceWidget.hide()

        textBox = QtWidgets.QFrame()
        textBox.setStyleSheet("""
            QFrame {
                background-color: white;
                border-top: 3px solid #b0c4ff;
            }
        """)
        textBox.setFixedHeight(160)

        textLayout = QtWidgets.QHBoxLayout(textBox)
        textLayout.setContentsMargins(40, 15, 40, 15)

        self.textLabel = QtWidgets.QLabel("ปกรณ์ที่ดูจะเหลี่ยมเหมือนมายคราฟ?\nฉันก็อยากหน้าเนียนกว่านี้เหมือนกันนะ ทำยังไงดีล่ะ??")
        self.textLabel.setWordWrap(True)
        self.textLabel.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
        self.textLabel.setStyleSheet("""
            color: #3A4E97;
            font-size: 20px;
            font-family: Candara;
        """)
        textLayout.addWidget(self.textLabel, stretch=1)

        # ---- Click button ----
        self.clickButton = QtWidgets.QPushButton("Click >>>")
        self.clickButton.setFixedSize(100, 40)
        self.clickButton.setCursor(QtCore.Qt.PointingHandCursor)
        self.clickButton.setStyleSheet("""
            QPushButton {
                color: #3A4E97;
                background-color: transparent;
                border: 2px solid #3A4E97;
                border-radius: 6px;
                font-size: 16px;
                font-family: Candara;
            }
            QPushButton:hover {
                background-color: #E6EBFF;
            }
        """)
        self.clickButton.clicked.connect(self.nextDialogue)
        textLayout.addWidget(self.clickButton, alignment=QtCore.Qt.AlignBottom)

        self.mainLayout.addWidget(textBox, stretch=1)

        self.dialogueIndex = 0
        self.dialogues = [
            "ปกรณ์ที่ดูจะเหลี่ยมเหมือนมายคราฟ?",
            "ปภรณ์อยากหน้าเนียนใส ทำเช่นไรดี??"
        ]

    def createChoiceButton(self, text, correct=False):
        btn = QtWidgets.QPushButton(text)
        btn.setFixedSize(350, 50)
        btn.setCursor(QtCore.Qt.PointingHandCursor)
        btn.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.3);
                color: white;
                font-size: 18px;
                border-radius: 10px;
                border: 2px solid rgba(255,255,255,0.5);
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.5);
            }
        """)
        if correct:
            btn.clicked.connect(self.correctChoice)
        else:
            btn.clicked.connect(self.wrongChoice)
        return btn

    def nextDialogue(self):
        self.dialogueIndex += 1
        if self.dialogueIndex < len(self.dialogues):
            self.textLabel.setText(self.dialogues[self.dialogueIndex])
        else:
            self.textLabel.setText("ว่าไง?")
            self.clickButton.hide()
            self.choiceWidget.show()

    def correctChoice(self):
        self.textLabel.setText("ทำแบบนั้นได้ด้วยนี่นา ขอบคุณนะ")
        self.choiceWidget.hide()
        self.clickButton.show()
        self.clickButton.setEnabled(False)

    def wrongChoice(self):
        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle("🤨 อาจารย์เต้ยไม่ถูกใจสิ่งนี้")
        msg.setText("พลาดแล้ว เธอมักง่ายนะ")
        msg.setStyleSheet("QLabel{color:#3A4E97; font-size:27px;}")
        msg.exec()
        QtCore.QTimer.singleShot(1000, self.close)  


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = LowPolyDialog()
    dialog.show()
    sys.exit(app.exec())
