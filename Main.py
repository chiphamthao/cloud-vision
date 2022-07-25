from ObjectDetector import ObjectDetector
from PyQt6.QtWidgets import QApplication

def main():
    app = QApplication([])
    demo = ObjectDetector()
    demo.show()
    app.exec()

if __name__ == "__main__":
    main()
