import sys, os, tempfile
from ObjectLocalization import ObjectLocalization
from TextRecognizer import TextRecognizer
from DragNDrop import DragNDrop
from TextToSpeech import TextToSpeech
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt, QUrl, QFileInfo
from PyQt6.QtGui import QPixmap
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer

class ObjectDetector(QWidget):

    def __init__(self):
        super().__init__()

        self.resize(500, 500)
        self.setAcceptDrops(True)

        self.mainLayout = QVBoxLayout()

        self.setWindowTitle("My app")
        self.photoViewer = DragNDrop()
        self.mainLayout.addWidget(self.photoViewer)
        self.mainLayout.addWidget(QLabel("Results: "))
    
        self.setLayout(self.mainLayout)

        btn = QPushButton('Play', clicked=self.playAudioFile)
        self.mainLayout.addWidget(btn)

        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()

        self.temp = tempfile.NamedTemporaryFile(suffix=".mp3")

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()

        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            
            event.setDropAction(Qt.DropAction.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.set_image(file_path)

            objectImage = TextRecognizer(file_path)
            result = objectImage.detect_text()
            showLabel = ObjectLocalization(file_path)
            objectList = showLabel.localize_objects()

            fullSentence = "The " + objectList[0] + " says " + result[1]
            print(fullSentence)
            self.showResults(result[0], fullSentence)

            event.accept()
        else:
            event.ignore()

    def set_image(self, file_path):
        self.photoViewer.setPixmap(QPixmap(file_path))

    def showResults(self, labels, sentence):
        for label in labels:
            print(label)
            self.mainLayout.addWidget(QLabel(label + ","))
            
        showSpeech = TextToSpeech(sentence, self.temp.name)
        showSpeech.text_to_speech()

    def playAudioFile(self):
        filename = self.temp.name
        self.player.setAudioOutput(self.audio_output)
        self.player.setSource(QUrl.fromLocalFile(filename))
        self.audio_output.setVolume(0.7)
        self.player.play()
        self.temp.close()


app = QApplication([])
demo = ObjectDetector()
demo.show()
app.exec()
