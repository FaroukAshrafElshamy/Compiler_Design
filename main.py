from PySide6.QtWidgets import QApplication,QMainWindow, QMenu, QWidget, QWidgetAction
from PySide6.QtCore import Qt
from ui_index3 import Ui_MainWindow
import sys

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("CodeX")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MySideBar()
    window.show()
    app.exec()
