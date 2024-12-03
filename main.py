from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtWebEngineWidgets import *
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from ui_index3 import Ui_MainWindow
import sys

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("CodeX")
        self.setWindowIcon(QIcon('resources/compiler(1).png'))

    # Connect Buttons
        self.ExplainButton.clicked.connect(self.S_Explain)
        self.EditorButton.clicked.connect(self.S_Editor)
        self.OutputButton.clicked.connect(self.S_Output)
        self.HubButton.clicked.connect(self.S_Hub)
        self.AboutButton.clicked.connect(self.S_About)
        self.ClearButton.clicked.connect(self.S_Clear)
        self.Open_file.clicked.connect(self.S_OpenFile)
        self.Save_file.clicked.connect(self.S_SaveFile)
        

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

    def S_Clear(self):
        self.textEdit.clear()

    def S_OpenFile(self):
        # Open a file dialog
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Text File", "", "Text Files (*.txt);;All Files (*)")
        if file_path:  # If a file is selected
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                self.textEdit.setPlainText(content)  # Display the content in QTextEdit
                self.fileName.setText(file_path)
            except Exception as e:
                self.textEdit.setPlainText(f"Failed to load the file.\nError: {e}")

    def S_SaveFile(self):
        # Open a file dialog for saving the file
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Text File", "", "Text Files (*.txt);;All Files (*)")
        if file_path:  # If a file path is provided
            try:
                with open(file_path, "w", encoding="utf-8") as file:
                    content = self.textEdit.toPlainText()  # Get content from QTextEdit
                    file.write(content)  # Write content to the file
            except Exception as e:
                self.text_edit.setPlainText(f"Failed to save the file.\nError: {e}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MySideBar()
    window.show()
    app.exec()
