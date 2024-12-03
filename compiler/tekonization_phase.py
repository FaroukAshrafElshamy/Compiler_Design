import re
from colorama import Fore

# Define token categories with regular expressions 
TOKEN_SPECIFICATION = [
    ('KEYWORD', r'\b(lo|mesh|print)\b'),  # Keywords
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),       # Identifiers
    ('NUMBER', r'\b\d+\b'),                          # Numbers
    ('OPERATOR', r'[+\-=<>]+'),                      # Operators
    ("STRING_LITERAL", r"\".*?\""),                  # Strings
    ("PUNCTUATION", r"[{}();]"),                     # Punctuation
    ('WHITESPACE', r'\s+'),                          # Whitespace (to skip)
]

# Compile regexes for token matching
def lexer(code):
    tokens = []
    pos = 0
    while pos < len(code):
        match = None
        for token_type, pattern in TOKEN_SPECIFICATION:
            regex = re.compile(pattern)
            match = regex.match(code, pos)
            if match:
                lexeme = match.group(0)
                if token_type != "WHITESPACE":  # Ignore whitespace
                    tokens.append((token_type, lexeme))
                pos = match.end()
                break
        if not match:
            raise ValueError(f"Unknown token at position {pos}: {code[pos]}")
    return tokens

    def read_file(file_path):
        with open(file_path, 'r') as file:
            return file.read()

if __name__ == '__main__':
    file_path = 'constants/code.txt'

    code = read_file(file_path)
    tokens = lexer(code)
    
    # Display tokens and their count
    print("Tokens:")
    print(f"Type\t\tLexeme")
    for token_type, lexeme in tokens:
        print(f"{Fore.MAGENTA}{token_type}\t{Fore.YELLOW}\t{lexeme}{Fore.RESET}")
    
#     print(f"{Fore.GREEN}\nTotal number of tokens: {Fore.RED}{len(tokens)}{Fore.RESET}")
