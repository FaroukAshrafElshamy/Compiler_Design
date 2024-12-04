import re
from colorama import Fore

def main(file_path, num = 2):
    # Define token categories with regular expressions 
    TOKEN_SPECIFICATION = [
        ('KEYWORD', r'\b(if|else)\b'),                   # Keywords
        ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),       # Identifiers
        ('NUMBER', r'\b\d+\b'),                          # Numbers
        ('OPERATOR', r'[+\-=<>]+'),                      # Operators
        ("STRING_LITERAL", r"\".*?\""),                  # Strings
        ("PUNCTUATION", r"[():]"),                     # Punctuation
        ('WHITESPACE', r'\s+'),                          # Whitespace (to skip)
    ]

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

                    if token_type != "WHITESPACE": 
                        tokens.append((token_type, lexeme))
                    pos = match.end()
                    break
            if not match:
                raise ValueError(f"Unknown token at position {pos}: {code[pos]}")
        return tokens

    def read_file(file_path):
        with open(file_path, 'r') as file:
            return file.read()
    
    code = read_file(file_path)
    tokens = lexer(code)
    
    if num == 1:
        with open("compiler/Output/tokens_output.txt", "w") as file:
            file.write("Tokens:\n")
            file.write(f"{'Type':<30}{'Lexeme'}\n")
            for token_type, lexeme in tokens:
                file.write(f"{token_type:<30}{lexeme}\n")
            file.write(f"\nTotal number of tokens: {len(tokens)}\n")
    
    elif num == 2:
        return code, tokens


# if __name__ == '__main__':
#     file_path = 'constants/code.txt'

    # code = read_file(file_path)
    # tokens = lexer(code)
    

#     print("Tokens:")
#     print(f"Type\t\tLexeme")
#     for token_type, lexeme in tokens:
#         print(f"{Fore.MAGENTA}{token_type}\t{Fore.YELLOW}\t{lexeme}{Fore.RESET}")
    
#     print(f"{Fore.GREEN}\nTotal number of tokens: {Fore.RED}{len(tokens)}{Fore.RESET}")
