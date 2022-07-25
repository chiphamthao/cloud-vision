from MainWidget import MainWidget
from PyQt6.QtWidgets import QApplication

def main():
    app = QApplication([])
    demo = MainWidget()
    demo.show()
    app.exec()

if __name__ == "__main__":
    main()
