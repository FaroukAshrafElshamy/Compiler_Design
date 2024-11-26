import re
import pandas as pd


# Define token categories with regular expressions for the new custom language syntax
token_specification = [
    ('KEYWORD',    r'\b(gimme|howto|call|maybe|else|repeat|giveback)\b'),  # Keywords
    ('TYPE',       r'\(num|txt|bool|fun\)'),                               # Type specifiers inside parentheses
    ('IDENTIFIER', r'[A-Za-z_]\w*'),                                       # Identifiers
    ('NUMBER',     r'\d+(\.\d*)?'),                                        # Integer or decimal number
    ('STRING',      r'"([^"\\]|\\.)*"'),  # String literal (anything inside double quotes, including escaped quotes)
    ('ASSIGN',     r'='),                                                  # Assignment operator
    ('OPERATOR',   r'[+\-*/]'),                                            # Arithmetic operators
    ('COMPARISON', r'==|!=|<=|>=|<|>'),                                    # Alternative comparison (not equal to)
    ('PUNCTUATION', r'[.,;]'),                                             # Punctuation
    ('PAREN',      r'[()]'),                                               # Parentheses
    ('BRACE',      r'[{}]'),                                               # Braces
    ('COMMENT',    r'#.*'),                                                # Comment from # to end of line
    ('END_CODE',   r';'),                                                  # End of code segment (semicolon)
    ('NEWLINE',    r'\n'),                                                 # Line endings
    ('SKIP',       r'[ \t]+'),                                             # Skip over spaces and tabs
    ('MISMATCH',   r'.'),                                                  # Any other character
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
            value = value[1:]  # Strip the '#' symbol from comments
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
    
    for token in tokens:
        print(token)

file_path = 'preDefined/program_1.txt'  
main(file_path)
