from .tokenization_phase import main
import pandas as pd
import json


def symbolTalbe(file_path):

    def get_the_identifiers_only():
        code, tokens = main(file_path, 2)
        identifiers = []
        for identifier in tokens:
            if identifier[0] == "IDENTIFIER":
                if identifier[1] not in identifiers:
                    identifiers.append(identifier[1])
        return identifiers


    def indexed_the_sourceCode():
        lines = []
        with open(file_path, "r") as file:
                for line_content in file:
                    lines.append(line_content.strip())
        return lines


    def get_line_appears(iden):
        lines = indexed_the_sourceCode()
        lines_for_IDEN = []
        for each in lines:
            if iden in each:
                lines_for_IDEN.append(lines.index(each)+1)
        line_declared = lines_for_IDEN[0]
        lines_of_usage = lines_for_IDEN[1:]
        return line_declared , lines_of_usage


    def getTypeAndSizeOfIden(iden):
        with open('compiler/Output/ParseTree.json', 'r') as file:
            data = json.load(file)  
            return data


    def find_value_of_iden(iden):
        data = getTypeAndSizeOfIden(iden)
        if isinstance(data, dict):
            for key, value in data.items():
                if key == '<program>':
                    for item in value:
                        if isinstance(item, dict) and '<variable_declaration>' in item:
                            identifier = item['<variable_declaration>'].get('<identifier>', None)
                            if identifier == iden:
                                expression = item['<variable_declaration>'].get('<expression>', {})
                                if expression.get('<digit>', None)  == None:
                                    return expression.get('<letter>', None)  
                                return expression.get('<digit>', None)  
        return None

  
    def determineTheTypeAndTheSizeOfTheIden(iden):
        value = find_value_of_iden(iden)
        iden_type = ""
        iden_size = 0
        try:
            value = int(value)
            iden_type = "Num"
            iden_size = 2
        except:
            iden_type = "Str"
            if isinstance(value,str):
                iden_size = len(value)
        return iden_type , iden_size    

    def show_the_code_indexed():
        with open(file_path, "r") as file:
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
        symbols.append(SymbolTalbe(iden,
                                   determineTheTypeAndTheSizeOfTheIden(iden)[0],
                                   determineTheTypeAndTheSizeOfTheIden(iden)[1],
                                   0,
                                   get_line_appears(iden)[0],
                                   get_line_appears(iden)[1]
                                   )
                       )

    data = [vars(symbol) for symbol in symbols]
    df = pd.DataFrame(data)

    # save on the csv file
    df.to_csv('compiler/Output/symbol_table.csv', index=False)

if __name__ == "__main__":
    # symbolTalbe("cof.txt")
    symbolTalbe('constants/code.txt')
