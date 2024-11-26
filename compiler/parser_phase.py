# Parser and Interpreter
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.ast = []

    def parse(self):
        while self.pos < len(self.tokens):
            self.ast.append(self.parse_function())
        return self.ast

    def parse_function(self):
        # Parse a function definition
        self.consume("KEYWORD", "fn")
        name = self.consume("IDENTIFIER")
        self.consume("PUNCTUATION", "(")
        self.consume("PUNCTUATION", ")")
        self.consume("PUNCTUATION", "{")
        body = []
        while self.peek()[1] != "}":
            body.append(self.parse_statement())
        self.consume("PUNCTUATION", "}")
        self.consume("PUNCTUATION", ";")
        return {"type": "function", "name": name, "body": body}

    def parse_statement(self):
        if self.peek()[0] == "KEYWORD":
            if self.peek()[1] == "atl3bra":
                return self.parse_print()
        elif self.peek()[0] == "IDENTIFIER":
            return self.parse_assignment()
        else:
            raise ValueError(f"Unexpected token {self.peek()}")

    def parse_print(self):
        self.consume("KEYWORD", "atl3bra")
        self.consume("PUNCTUATION", "(")
        content = self.consume("STRING_LITERAL")
        self.consume("PUNCTUATION", ")")
        self.consume("PUNCTUATION", ";")
        return {"type": "print", "value": content}

    def parse_assignment(self):
        var_name = self.consume("IDENTIFIER")
        self.consume("OPERATOR", "=")
        value = self.consume("NUMBER")
        self.consume("PUNCTUATION", ";")
        return {"type": "assignment", "name": var_name, "value": value}

    def consume(self, expected_type, expected_value=None):
        token = self.tokens[self.pos]
        if token[0] != expected_type or (expected_value and token[1] != expected_value):
            raise ValueError(f"Expected {expected_type} {expected_value}, but got {token}")
        self.pos += 1
        return token[1]

    def peek(self):
        return self.tokens[self.pos]

class Interpreter:
    def __init__(self, ast):
        self.ast = ast
        self.variables = {}

    def execute(self):
        for node in self.ast:
            if node["type"] == "function":
                self.execute_function(node)

    def execute_function(self, node):
        for statement in node["body"]:
            self.execute_statement(statement)

    def execute_statement(self, node):
        if node["type"] == "print":
            print(node["value"].strip('"'))
        elif node["type"] == "assignment":
            self.variables[node["name"]] = int(node["value"])
        else:
            raise ValueError(f"Unknown statement type: {node['type']}")
        

tokens = lexer(code)
parser = Parser(tokens)
ast = parser.parse()

interpreter = Interpreter(ast)
interpreter.execute()