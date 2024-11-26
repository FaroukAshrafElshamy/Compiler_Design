
import re

# Define token categories with regular expressions 
TOKEN_SPECIFICATION = [
    ('KEYWORD', r'\b(fn|lo|mesh|floop|atl3bra)\b'),  # Keywords
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),       # Identifiers
    ('NUMBER', r'\b\d+\b'),                          # Numbers
    ('STRING', r'"[^"]*"'),                          # Strings
    ('OPERATOR', r'[+\-*/=<>!]+'),                   # Operators
    ('DELIMITER', r'[{}()]'),                        # Braces and parentheses
    ('SEPARATOR', r'[,;]'),                             # Separator
    ('WHITESPACE', r'\s+'),                          # Whitespace (to skip)
    ('MISMATCH', r'.'),                              # Any other character
]

# Compile regexes for token matching
token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPECIFICATION)

def lex(code):
    """
    Tokenize the given code into type, token, and lexeme.
    """
    tokens = []
    for match in re.finditer(token_regex, code):
        token_type = match.lastgroup
        lexeme = match.group(token_type)
        if token_type == 'WHITESPACE':
            continue  # Skip whitespace
        elif token_type == 'MISMATCH':
            raise SyntaxError(f'Unexpected character: {lexeme}')
        tokens.append((token_type, lexeme))
    return tokens

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Main program
if __name__ == '__main__':
    # Specify the file containing the code
    file_path = 'preDefined/program_1.txt'

    # Read code from the file
    code = read_file(file_path)
    tokens = lex(code)
    for token in tokens:
        print(token)
