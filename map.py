
import re
import pandas as pd

# Define token categories with regular expressions for the custom language
token_specification = [
    ('KEYWORD',    r'\b(fn|floop|wloop|lo|mesh|shout)\b'),  # Keywords
    ('TYPE',       r'\((T|i|f|s|b|l)\)'),                  # Type specifiers inside parentheses
    ('IDENTIFIER', r'[A-Za-z_]\w*'),                       # Identifiers
    ('NUMBER',     r'\d+(\.\d*)?'),                        # Integer or decimal number
    ('ASSIGN',     r'='),                                  # Assignment operator
    ('INCREMENT',  r'\+\+'),                               # Increment
    ('DECREMENT',  r'--'),                                 # Decrement
    ('COMPARISON', r'=='),                                 # Comparison
    ('ALT_COMP',   r'><'),                                 # Alternative comparison
    ('OPERATOR',   r'[+\-*/]'),                            # Arithmetic operators
    ('PUNCTUATION', r'[.,;]'),                             # Punctuation
    ('PAREN',      r'[()]'),                               # Parentheses
    ('BRACE',      r'[{}]'),                               # Braces
    ('BRACKET',    r'[\[\]]'),                             # Brackets
    ('COMMENT',    r'\$.*'),                               # Comment from `$` to end of line
    ('END_CODE',   r'!'),                                  # End of code segment
    ('NEWLINE',    r'\n'),                                 # Line endings
    ('SKIP',       r'[ \t]+'),                             # Skip over spaces and tabs
    ('MISMATCH',   r'.'),                                  # Any other character
]

# Compile regexes for token matching
token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
token_pattern = re.compile(token_regex)

def lexeme_analyzer(text):
    tokens = []
    for match in token_pattern.finditer(text):
        kind = match.lastgroup
        value = match.group(kind)
        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        elif kind == 'SKIP' or kind == 'NEWLINE':
            continue  # Ignore whitespace and newlines
        elif kind == 'COMMENT':
            value = value[1:]  # Strip the `$` symbol from comments
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character {value!r}')
        tokens.append((kind, value))
    return tokens

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def main(file_path):
    # Read and analyze the file content
    content = read_file(file_path)
    tokens = lexeme_analyzer(content)
    
    # Create and print the tokens table
    df = pd.DataFrame(tokens, columns=['Token Type', 'Lexeme'])
    print(df)

# Run the main function with the path to your text file
file_path = 'test.txt'  # Replace with your file path
main(file_path)
