from PySide6 import QtCore, QtGui, QtWidgets
import sys

ROOT_RESOURCE_DIR = r'C:/Users/jajap/OneDrive/Documents/maya/2026/scripts'

class BrokenTexturesDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('🤓 Broken Textures Route')
        self.resize(890, 650)
        self.setStyleSheet('background-color: #6095FE;')

        self.mainLayout = QtWidgets.QVBoxLayout(self)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(0)

        self.imageLabel = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap(f'{ROOT_RESOURCE_DIR}/Lets_flirt_Papakorn/images/Broken.png')
        scaled_pixmap = pixmap.scaled(
            QtCore.QSize(890, 500),
            QtCore.Qt.KeepAspectRatio,
            QtCore.Qt.SmoothTransformation
        )
        self.imageLabel.setPixmap(scaled_pixmap)
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setStyleSheet('background-color: transparent;')
        self.mainLayout.addWidget(self.imageLabel, stretch=4)

        self.choiceWidget = QtWidgets.QWidget()
        self.choiceLayout = QtWidgets.QVBoxLayout(self.choiceWidget)
        self.choiceLayout.setAlignment(QtCore.Qt.AlignCenter)
        self.choiceLayout.setSpacing(15)
        self.choiceWidget.setStyleSheet('background: transparent;')
        self.mainLayout.addWidget(self.choiceWidget, alignment=QtCore.Qt.AlignCenter)
        self.choiceWidget.hide()

        textBox = QtWidgets.QFrame()
        textBox.setStyleSheet('''
            QFrame {
                background-color: white;
                border-top: 3px solid #b0c4ff;
            }
        ''')
        textBox.setFixedHeight(160)

        textLayout = QtWidgets.QHBoxLayout(textBox)
        textLayout.setContentsMargins(40, 15, 40, 15)

        self.textLabel = QtWidgets.QLabel()
        self.textLabel.setTextFormat(QtCore.Qt.RichText)
        self.textLabel.setWordWrap(True)
        self.textLabel.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
        self.textLabel.setStyleSheet('''
            color: #3A4E97;
            font-size: 20px;
            font-family: Candara;
        ''')
        textLayout.addWidget(self.textLabel, stretch=1)

        self.clickButton = QtWidgets.QPushButton('Click >>>')
        self.clickButton.setFixedSize(100, 40)
        self.clickButton.setCursor(QtCore.Qt.PointingHandCursor)
        self.clickButton.setStyleSheet('''
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
        ''')
        self.clickButton.clicked.connect(self.nextDialogue)
        textLayout.addWidget(self.clickButton, alignment=QtCore.Qt.AlignBottom)

        self.mainLayout.addWidget(textBox, stretch=1)

        self.scenes = [
            {
                'text': '<b>ปภกรณ์ที่ทำไมใบหน้าแกไปคนละทิศจังวะเห้ย?</b><br>'
                        '"เห็นเขาบอกเธอช่วยแก้ข้อผิดพลาดได้"',
                'choices': [
                    {'text': 'ได้สิ เรียนมาขนาดนี้ละ', 'correct': True},
                    {'text': 'ไม่อะ เคสแบบนายหนักอยู่นะ', 'correct': False}
                ]
            },
            {
                'text': '<b>ปภกรณ์ที่ทำไมใบหน้าแกไปคนละทิศจังวะเห้ย?</b><br>'
                        '"งั้นเคสแบบฉันควรแก้ยังไงล่ะ?"',
                'choices': [
                    {'text': 'เข้า UV แล้วสร้างใหม่\nถ้าให้ดีนายต้องเชื่อมเองด้วย', 'correct': True},
                    {'text': 'UV auto สิจ้ะ', 'correct': False}
                ]
            },
            {
                'text': '<b>ปภกรณ์ที่ทำไมใบหน้าแกไปคนละทิศจังวะเห้ย?</b><br>'
                        '"รู้ดีจริงนะ อนาคตทรีดีอาร์ตติสหรือเปล่าเนี่ย"',
                'choices': [
                    {'text': 'บ่ จะจบออกไปขายก๋วยเตี๋ยว', 'correct': False},
                    {'text': 'ถ้าเป็นได้น่ะนะ', 'correct': True}
                ]
            }
        ]

        self.sceneIndex = 0
        self.waitingNextScene = False
        self.showScene(self.scenes[self.sceneIndex])

    def createChoiceButton(self, text, correct=False):
        btn = QtWidgets.QPushButton(text)
        btn.setFixedSize(350, 50)
        btn.setCursor(QtCore.Qt.PointingHandCursor)
        btn.setStyleSheet('''
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
        ''')
        if correct:
            btn.clicked.connect(self.correctChoice)
        else:
            btn.clicked.connect(self.wrongChoice)
        return btn

    def showScene(self, scene):
        self.textLabel.setText(scene['text'])
        self.choiceWidget.hide()
        self.clickButton.show()
        if scene['choices']:
            self.updateChoices(scene['choices'])
        else:
            for i in reversed(range(self.choiceLayout.count())):
                self.choiceLayout.itemAt(i).widget().deleteLater()
        self.waitingNextScene = False

    def updateChoices(self, choices):
        for i in reversed(range(self.choiceLayout.count())):
            self.choiceLayout.itemAt(i).widget().deleteLater()
        for c in choices:
            btn = self.createChoiceButton(c['text'], correct=c['correct'])
            self.choiceLayout.addWidget(btn)

    def nextDialogue(self):
        if self.waitingNextScene:
            self.sceneIndex += 1
            if self.sceneIndex < len(self.scenes):
                self.showScene(self.scenes[self.sceneIndex])
            else:
                self.textLabel.setText('(ท่าทางเขาดูให้กำลังใจคุณอยู่)\nปภกรณ์ชื่นชมคุณมาก ได้รับหัวใจหนึ่งดวง 💙')
                self.clickButton.hide()
        else:
            current_scene = self.scenes[self.sceneIndex]
            if current_scene['choices']:
                self.choiceWidget.show()
                self.clickButton.hide()
            else:
                self.sceneIndex += 1
                if self.sceneIndex < len(self.scenes):
                    self.showScene(self.scenes[self.sceneIndex])
                else:
                    self.textLabel.setText('(ท่าทางเขาดูให้กำลังใจคุณอยู่)\nปภกรณ์ชื่นชมคุณมาก ได้รับหัวใจหนึ่งดวง 💙')
                    self.clickButton.hide()

    def correctChoice(self):
        if self.sceneIndex == 0:
            self.textLabel.setText('<b>ปภกรณ์ที่ทำไมใบหน้าแกไปคนละทิศจังวะเห้ย?</b><br>'
                                   '"งั้นขอพิสูจน์หน่อยละกัน"')
        elif self.sceneIndex == 1:
            self.textLabel.setText('<b>ปภกรณ์ที่ทำไมใบหน้าแกไปคนละทิศจังวะเห้ย?</b><br>'
                                   '"เกมต่อจิ๊กซอว์ดี ๆ นี่เอง"')
        elif self.sceneIndex == 2:
            self.textLabel.setText('<b>ปภกรณ์ที่ทำไมใบหน้าแกไปคนละทิศจังวะเห้ย?</b><br>'
                                   '"เป็นได้อยู่แล้ว ฉันเชื่อในตัวเธอนะ"')

            new_pixmap = QtGui.QPixmap(f"{ROOT_RESOURCE_DIR}/Lets_flirt_Papakorn/images/Broken_smile.png")
            scaled_pixmap = new_pixmap.scaled(
                QtCore.QSize(890, 500),
                QtCore.Qt.KeepAspectRatio,
                QtCore.Qt.SmoothTransformation
            )
            self.imageLabel.setPixmap(scaled_pixmap)

        self.choiceWidget.hide()
        self.clickButton.show()
        self.waitingNextScene = True

    def wrongChoice(self):
        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle('🤨 ตอบงี้ตั้งใจเรียนหรือเปล่า')
        msg.setText('"ทำตัวดี ๆ ลูก เราเป็นไอซีที"')
        msg.setStyleSheet('QLabel{color:#3A4E97; font-size:27px;}')
        msg.exec()
        QtCore.QTimer.singleShot(1000, self.close)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = LowPolyDialog()
    dialog.show()
    sys.exit(app.exec())
