import re
from colorama import Fore

def main(file_path):
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
        Tokens = []
        pos = 0
        while pos < len(code):
            match = None
            for token_type, pattern in TOKEN_SPECIFICATION:
                regex = re.compile(pattern)
                match = regex.match(code, pos)
                if match:
                    lexeme = match.group(0)
                    if token_type != "WHITESPACE":  # Ignore whitespace
                        Tokens.append((token_type, lexeme))
                    pos = match.end()
                    break
            if not match:
                raise ValueError(f"Unknown token at position {pos}: {code[pos]}")
        return Tokens

    def read_file(file_path):
        with open(file_path, 'r') as file:
            return file.read()

    code = read_file(file_path)
    tokens = lexer(code)

    # Open a file for writing
    with open("tokens_output.txt", "w") as file:
        file.write("Tokens:\n")
        file.write(f"{'Type':<15}{'Lexeme'}\n")
        for token_type, lexeme in tokens:
            file.write(f"{Fore.MAGENTA}{token_type:<15}{Fore.YELLOW}{lexeme}{Fore.RESET}\n")
        
        file.write(f"{Fore.GREEN}\nTotal number of tokens: {Fore.RED}{len(tokens)}{Fore.RESET}\n")





# if __name__ == '__main__':
#     file_path = 'constants/code.txt'

#     code = read_file(file_path)
#     tokens = lexer(code)
    
#     # Display tokens and their count
#     print("Tokens:")
#     print(f"Type\t\tLexeme")
#     for token_type, lexeme in tokens:
#         print(f"{Fore.MAGENTA}{token_type}\t{Fore.YELLOW}\t{lexeme}{Fore.RESET}")
    
#     print(f"{Fore.GREEN}\nTotal number of tokens: {Fore.RED}{len(tokens)}{Fore.RESET}")
