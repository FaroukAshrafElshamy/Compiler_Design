def First():

    def CalculateFirst(obj):
        if obj in First_Dic:
            return First_Dic[obj]
        First_Dic[obj] = set()

        for production in Grammar.get(obj, []):
            rules = production.split()
            for rule in rules:
                if isTerminal(rule):
                    First_Dic[obj].add(rule)
                    break
                else:
                    First_Dic[obj].update(CalculateFirst(rule) - {""})
                    if "" not in First_Dic[rule]:
                        break
        return First_Dic[obj]


    def isTerminal(obj):
        if obj not in Grammar or obj in ["[A-Z]", "[a-z]", "[0-9]", "_"]:
            return True
        else:
            return False

    First_Dic = {}
    Grammar = {
            "<program>": ["<statement>"],
            "<statement>": ["<variable_declaration>", "<condition_statement>"],
            "<variable_declaration>": ["<identifier> = <expression>"],
            "<condition_statement>": ["if ( <condition> ) : <statement>", "else : <statement>"],
            "<condition>": ["<expression> <comparison_operator> <expression>"],
            "<comparison_operator>": ["==", "=!", "<", ">", "<=", ">="],
            "<expression>": ["<identifier>", "<literal>"],
            "<literal>": ["<digit>", "<string_literal>"],
            "<string_literal>" : [ "<letter>"],
            "<identifier>": ["<letter>", "<letter> <all_list>"],
            "<all_list>": ["<letter>", "<digit>", "_"],
            "<digit>": ["[0:9]"],
            "<letter>": ["[a-z]", "[A-Z]"],
        }


    for non_terminal in Grammar:
        CalculateFirst(non_terminal)

    output_file = "compiler/Output/FIRST_output.txt"
    with open(output_file, "w", encoding="utf-8") as file:
        for non_terminal, s_first in First_Dic.items():
            line = f"First({non_terminal[1:len(non_terminal)-1]})".ljust(29) + f"==>  {sorted(s_first)}\n"
            file.write(line)


if __name__ == "__main__":
    First()
