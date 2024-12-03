def terminal(obj):
    return obj not in GRAMMER or obj in ["[A-Z]", "[a-z]", "[0-9]", "_"]

def first(obj):

    if obj in FIRST:
        return FIRST[obj]
    FIRST[obj] = set()

    for product in GRAMMER.get(obj, []):
        grammers = product.split()
        for txt in grammers:
            if terminal(txt):
                if txt == "[A-Z]":
                    FIRST[obj].update(chr(c) for c in range(ord('A'), ord('Z') + 1))
                elif txt == "[a-z]":
                    FIRST[obj].update(chr(c) for c in range(ord('a'), ord('z') + 1))
                elif txt == "[0-9]":
                    FIRST[obj].update(chr(c) for c in range(ord('0'), ord('9') + 1))
                elif txt == "_":
                    FIRST[obj].add("_")
                elif txt == "(":
                    FIRST[obj].add("(")
                else:
                    FIRST[obj].add(txt)
                break
            else:
                FIRST[obj].update(first(txt) - {"\""})
                if "" not in FIRST[txt]:
                    break
    return FIRST[obj]

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
for non_terminal in GRAMMER:
    first(non_terminal)

for non_terminal, s_first in FIRST.items():
    print(f"First({non_terminal})          \t ==> \t{sorted(s_first)}")
    
    