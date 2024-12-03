import re
from tokenization_phase import *
GRAMMAR = {
    "<program>": ["<statement>"],
    "<statement>": ["<variable_declaration>", "<condition_statement>"],
    "<variable_declaration>": ["<identifier> = <expression>"],
    "<condition_statement>": ["if ( <condition> ) : <statement>", "else : <statement>"],
    "<condition>": ["<expression> <comparison_operator> <expression>"],
    "<comparison_operator>": ["==", "!= ", "<", ">", "<=", ">="],
    "<expression>": ["<identifier>", "<literal>"],
    "<literal>": ["<digit>", "<string_literal>"],
    "<string_literal>": ['" <letter>* "'],
    "<identifier>": ["<letter>", "<letter><all_list>*"],
    "<all_list>": ["<letter>", "<digit>", "_"],
    "<digit>": ["[0-9]+"],
    "<letter>": ["[a-zA-Z]"],
}

class ParseTreeNode:
    def __init__(self, value):
        self.value = value  # Non-terminal/terminal
        self.children = []  # Children nodes

    def add_child(self, child):
        self.children.append(child)

    def __str__(self, level=0):
        ret = "  " * level + repr(self.value) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def __repr__(self):
        return f"{self.value}"


def tokenize(source_code):
    tokens = lexer(source_code)
    return tokens


def parse(non_terminal, tokens):
    """Parse tokens based on the grammar and construct the parse tree."""
    if not tokens:
        return None, tokens

    for rule in GRAMMAR.get(non_terminal, []):
        # Split the rule into components
        rule_components = rule.split()
        temp_tokens = tokens[:]  # Copy of the tokens for backtracking
        node = ParseTreeNode(non_terminal)
        match = True

        for component in rule_components:
            if component in GRAMMAR:  # Non-terminal
                child, temp_tokens = parse(component, temp_tokens)
                if child is None:
                    match = False
                    break
                node.add_child(child)
            else:  # Terminal
                if temp_tokens and re.fullmatch(component, temp_tokens[0]):
                    node.add_child(ParseTreeNode(temp_tokens.pop(0)))
                else:
                    match = False
                    break

        if match:
            return node, temp_tokens

    return None, tokens  # No match found


def parse_tree(source_code):
    tokens = tokenize(source_code)
    print(f"Tokens: {tokens}")
    tree, remaining_tokens = parse("<program>", tokens)
    if remaining_tokens:
        print(f"Error: Unparsed tokens remain: {remaining_tokens}")
        return None
    return tree


if __name__ == "__main__":
    # Example input
    source_code = 'if ( x == 10 ) : y = 5'
    tree = parse_tree(source_code)
    if tree:
        print("\nParse Tree:")
        print(tree)
