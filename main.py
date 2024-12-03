from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem
from ui_index3 import Ui_MainWindow
from compiler.tokenization_phase import main
from compiler.symbol_table import symbolTalbe
from compiler.parser_phase import visulize, parser
from PySide6.QtGui import QIcon
from compiler.First import First
import csv
import sys


class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("CodeX")
        self.setWindowIcon(QIcon('resources/compiler(1).png'))
        self.TabSize(7) # Tab Size

    # Connect Buttons
        self.ExplainButton.clicked.connect(self.S_Explain)
        self.EditorButton.clicked.connect(self.S_Editor)
        self.OutputButton.clicked.connect(self.S_Output)
        self.HubButton.clicked.connect(self.S_Hub)
        self.AboutButton.clicked.connect(self.S_About)
        self.ClearButton.clicked.connect(self.S_Clear)
        self.Open_file.clicked.connect(self.S_OpenFile)
        self.Save_file.clicked.connect(self.S_SaveFile)
        self.RunButton.clicked.connect(self.OutputTokens)
        self.RunButton.clicked.connect(self.OutputFirst)
        self.RunButton.clicked.connect(self.OutputSymboleTable)
        self.RunButton.clicked.connect(self.OutputParse)
        self.FigureButton.clicked.connect(visulize)
        

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
        self.fileName.clear()

    def S_OpenFile(self):
        global file_path
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Text File", "", "Text Files (*.txt);;All Files (*)")
        main(file_path, 1)
        symbolTalbe(file_path)
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                self.textEdit.setPlainText(content)
                self.fileName.setText(file_path)
            except Exception as e:
                self.textEdit.setPlainText(f"Failed to load the file.\nError: {e}")

    def S_SaveFile(self):
        file_path2, _ = QFileDialog.getSaveFileName(self, "Save Text File", "", "Text Files (*.txt);;All Files (*)")
        if file_path2:
            try:
                with open(file_path2, "w", encoding="utf-8") as file:
                    content = self.textEdit.toPlainText()
                    file.write(content)
                main(file_path2, 1)
                symbolTalbe(file_path2)
                parser(file_path2)
            except Exception as e:
                self.text_edit.setPlainText(f"Failed to save the file.\nError: {e}")

    def TabSize(self, space_count):
        font_metrics = self.textEdit.fontMetrics()
        space_width = font_metrics.horizontalAdvance(' ')
        self.textEdit.setTabStopDistance(space_width * space_count)

    def OutputTokens(self):
        self.TextOutput.clear()
        output_path = "compiler/Output/tokens_output.txt"
        if output_path:
            try:
                with open(output_path, "r", encoding="utf-8") as file:
                    content = file.read()
                self.TextOutput.append(content)
            except Exception as e:
                self.TextOutput.append(f"Failed to append the file.\nError: {e}")

    def OutputFirst(self):
        First()
        self.TextOutput3.clear()
        output_path = "compiler/Output/FIRST_output.txt"
        if output_path:
            try:
                with open(output_path, "r", encoding="utf-8") as file:
                    content = file.read()
                self.TextOutput3.append(content)
            except Exception as e:
                self.TextOutput3.append(f"Failed to append the file.\nError: {e}")

    def OutputParse(self):
        parser(file_path)
        self.TextOutput2.clear()
        output_path = "compiler/Output/ParseTree.json"
        if output_path:
            try:
                with open(output_path, "r", encoding="utf-8") as file:
                    content = file.read()
                self.TextOutput2.append(content)
            except Exception as e:
                self.TextOutput2.append(f"Failed to append the file.\nError: {e}")

    def OutputSymboleTable(self):
        self.tableWidget.clear()
        output_path = 'compiler/Output/symbol_table.csv'
        if output_path:
            try:
                with open(output_path, "r", encoding="utf-8") as file:
                    reader = csv.reader(file)
                    data = list(reader)
                if data:
                    self.tableWidget.setRowCount(len(data))
                    self.tableWidget.setColumnCount(len(data[0]))
                    for row_idx, row in enumerate(data):
                        for col_idx, cell in enumerate(row):
                            self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(cell))
            except Exception as e:
                print(f"Error reading file: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MySideBar()
    window.show()
    app.exec()
