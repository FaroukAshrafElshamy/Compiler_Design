
GRAMMER = {
    "<program>": ["<statement>"],
    "<statement>": ["<variable_declaration>", "<condition_statement>"],
    "<variable_declaration>": ["<identifier> = <expression>"],
    "<condition_statement>": ["if ( <condition> ) : <statement>", "else : <statement>"],
    "<condition>": ["<expression> <comparison_operator> <expression>"],
    "<comparison_operator>": ["==", "=!", "<", ">", "<=", ">="],
    "<expression>": ["<identifier>", "<literal>"],
    "<literal>": ["<digit>", "<string_literal>"],
    "<string_literal>" : [ "\" <letter>* \""],
    "<identifier>": ["<letter>", "<letter> <all_list>"],
    "<all_list>": ["<letter>", "<digit>", "_"],
    "<digit>": ["[0:9]"],
    "<letter>": ["[a-zA-Z]"],
}


FIRST = {}

def is_terminal(obj):
    return obj not in GRAMMER or obj in ["[A-Z]", "[a-z]", "[0-9]", "_"]

def get_first(obj):

    if obj in FIRST:
        return FIRST[obj]
    FIRST[obj] = set()

    for product in GRAMMER.get(obj, []):
        parts = product.split()
        for part in parts:
            if is_terminal(part):
                if part == "[A-Z]":
                    FIRST[obj].update(chr(c) for c in range(ord('A'), ord('Z') + 1))
                elif part == "[a-z]":
                    FIRST[obj].update(chr(c) for c in range(ord('a'), ord('z') + 1))
                elif part == "[0-9]":
                    FIRST[obj].update(chr(c) for c in range(ord('0'), ord('9') + 1))
                elif part == "_":
                    FIRST[obj].add("_")
                elif part == "(":
                    FIRST[obj].add("(")
                else:
                    FIRST[obj].add(part)
                break
            else:
                FIRST[obj].update(get_first(part) - {"\""})
                if "" not in FIRST[part]:
                    break
    return FIRST[obj]

for non_terminal in GRAMMER:
    get_first(non_terminal)

for non_terminal, first_set in FIRST.items():
    print(f"First({non_terminal})          \t ==> \t{sorted(first_set)}")
    
    