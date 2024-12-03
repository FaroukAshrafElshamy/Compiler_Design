from tokenization_phase import lexer, read_file

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def match(self, *expected_types):
        """Consume a token if it matches any of the expected types."""
        if self.current < len(self.tokens) and self.tokens[self.current][0] in expected_types:
            token = self.tokens[self.current]
            self.current += 1
            return token
        return None
    

    def parse_statement(self):
        node = None
        if self.match("IDENTIFIER"):
            self.current -= 1  
            node = self.parse_variable_declaration()
        elif self.match("KEYWORD", "if"):
            self.current -= 1  
            node = self.parse_condition_statement()
        return node

    def parse_variable_declaration(self):
        identifier = self.match("IDENTIFIER")
        self.match("OPERATOR")  
        expression = self.parse_expression()
        return ("variable_declaration", identifier, expression)

    def parse_condition_statement(self):
        if_token = self.match("if")
        self.match("PUNCTUATION")  
        condition = self.parse_condition()
        self.match("PUNCTUATION")  
        self.match("PUNCTUATION")  
        true_branch = self.parse_statement()
        else_branch = None
        if self.match("else"):
            self.match("PUNCTUATION")
            else_branch = self.parse_statement()
        return ("condition", condition, true_branch, else_branch)

    def parse_condition(self):
        left = self.parse_expression()
        operator = self.match("OPERATOR")
        right = self.parse_expression()
        return ("condition", left, operator, right)

    def parse_expression(self):
        token = self.match("IDENTIFIER", "NUMBER", "STRING_LITERAL")
        if token:
            return ("expression", token)
        
        
file_path = './constants/code.txt'

code = read_file(file_path)

tokens = lexer(code)
parser = Parser(tokens)
print(parser.tokens)
parse_tree = parser.parse_statement()

print(parse_tree)


parser = Parser(tokens)
parse_tree = parser.parse_statement()

print(parse_tree)