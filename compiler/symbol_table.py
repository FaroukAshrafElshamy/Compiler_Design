
from tekonization_phase import *
import pandas as pd

def get_the_identifiers_only():
    file_path = 'constants/code.txt'
    code = read_file(file_path)
    tokens = lexer(code)
    
    identifiers = []
    for identifier in tokens:
        if identifier[0] == "IDENTIFIER":
            if identifier[1] not in identifiers:
                identifiers.append(identifier[1])
    
    return identifiers


def numbers_file():
    lines = []
    with open('constants/code.txt', "r") as file:
            for line_content in file:
                lines.append(line_content.strip())
    return lines

def get_line_appears(iden):
    lines = numbers_file()
    lines_for_IDEN = []
    for each in lines:
        if iden in each:
            lines_for_IDEN.append(lines.index(each)+1)
    line_declared = lines_for_IDEN[0]
    lines_of_usage = lines_for_IDEN[1:]
    return line_declared , lines_of_usage



def show_the_code_indexed():
    with open('constants/code.txt', "r") as file:
            for line_number, line_content in enumerate(file, start=1):
                print(f"Line {line_number}: {line_content.strip()}")



class SymbolTalbe:
    def __init__(self, name, type, size, dim, lineDeclared, linesOfUsage) -> None:
        self.name = name
        self.type = type
        self.size = size
        self.dim = dim
        self.lineDeclared = lineDeclared
        self.lineOfUsage = linesOfUsage





symbols = []

for iden in get_the_identifiers_only():
    symbols.append(SymbolTalbe(iden,"null","null",0,get_line_appears(iden)[0],get_line_appears(iden)[1]))



data = [vars(symbol) for symbol in symbols]
df = pd.DataFrame(data)
print(df)
