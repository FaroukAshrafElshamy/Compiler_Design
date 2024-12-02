from PySide6.QtWidgets import QApplication,QMainWindow
# from Custom_Widgets.Widgets import *
from PySide6.QtCore import Qt
from ui_index3 import Ui_MainWindow
import sys

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("CodeX")
        # loadJsonStyle(self, self.ui)

    # Connect Buttons
        self.ExplainButton.clicked.connect(self.S_Explain)
        self.EditorButton.clicked.connect(self.S_Editor)
        self.OutputButton.clicked.connect(self.S_Output)
        self.HubButton.clicked.connect(self.S_Hub)
        self.AboutButton.clicked.connect(self.S_About)

    # Add pdf
        # self.

    # Methods to switch to different pages
    def S_Explain(self):
        self.Main_page.setCurrentIndex(0)

    def S_Editor(self):
        self.Main_page.setCurrentIndex(1)

    def S_Output(self):
        self.Main_page.setCurrentIndex(2)

    def S_Hub(self):
        self.Main_page.setCurrentIndex(3)

    def S_About(self):
        self.Main_page.setCurrentIndex(4)




if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MySideBar()
    window.show()
    app.exec()
