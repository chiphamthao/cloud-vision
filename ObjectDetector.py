import sys, os
from vision_cloud_ocr import TextRecognitor
from ImageLabel import ImageLabel
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

class ObjectDetector(QWidget, TextRecognitor):
    def __init__(self):
        super().__init__()

        self.resize(500, 500)
        self.setAcceptDrops(True)

        self.mainLayout = QVBoxLayout()

        self.setWindowTitle("My app")
        self.photoViewer = ImageLabel()
        self.mainLayout.addWidget(self.photoViewer)
        self.mainLayout.addWidget(QLabel("Results: "))
    
        self.setLayout(self.mainLayout)

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
            self.detect_text(file_path)
            self.showResults(self.labels)

            event.accept()
        else:
            event.ignore()

    def set_image(self, file_path):
        self.photoViewer.setPixmap(QPixmap(file_path))

    def showResults(self, labels):
        print(len(labels))
        for label in labels:
            print(label)
            self.mainLayout.addWidget(QLabel(label + ", "))

app = QApplication([])
demo = ObjectDetector()
demo.show()
app.exec()