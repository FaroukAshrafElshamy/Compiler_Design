from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui_index3 import Ui_MainWindow
from PySide6.QtGui import QIcon
from compiler.tekonization_phase import main
import sys

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("CodeX")
        self.setWindowIcon(QIcon('resources/compiler(1).png'))
        self.TabSize(5) # Tab Size

    # Connect Buttons
        self.ExplainButton.clicked.connect(self.S_Explain)
        self.EditorButton.clicked.connect(self.S_Editor)
        self.OutputButton.clicked.connect(self.S_Output)
        self.HubButton.clicked.connect(self.S_Hub)
        self.AboutButton.clicked.connect(self.S_About)
        self.ClearButton.clicked.connect(self.S_Clear)
        self.Open_file.clicked.connect(self.S_OpenFile)
        self.Save_file.clicked.connect(self.S_SaveFile)
        self.RunButton.clicked.connect(self.append_file) ##############
        

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
        self.TextOutput.clear()

    def S_OpenFile(self):
        global file_path
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Text File", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
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

    def TabSize(self, space_count):
        font_metrics = self.textEdit.fontMetrics()
        space_width = font_metrics.horizontalAdvance(' ')
        self.textEdit.setTabStopDistance(space_width * space_count)


    def append_file(self):
        # (file_path)
        # file_path, _ = QFileDialog.getOpenFileName(self, "Select Text File to Append", "", "Text Files (*.txt);;All Files (*)")
        main(file_path)
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                self.TextOutput.append(content)
            except Exception as e:
                self.TextOutput.append(f"Failed to append the file.\nError: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MySideBar()
    window.show()
    app.exec()
