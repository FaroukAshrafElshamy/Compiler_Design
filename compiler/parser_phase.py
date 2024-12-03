from tokenization_phase import lexer, read_file
# Parser and Interpreter
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        statements = []
        while self.pos < len(self.tokens):
            if self.peek()[1] in ("lo", "lomesh", "mesh"):
                statements.append(self.parse_condition())
            else:
                statements.append(self.parse_assignment())
        return statements

    def parse_condition(self):
        condition_type = self.consume("KEYWORD")
        if condition_type == "mesh":
            condition = None
        else:
            self.consume("PUNCTUATION", "(")
            left = self.consume("IDENTIFIER")
            operator = self.consume("OPERATOR")
            right = self.consume("NUMBER")
            self.consume("PUNCTUATION", ")")
            condition = (left, operator, int(right))
        self.consume("PUNCTUATION", "{")
        body = []
        while self.peek()[1] != "}":
            body.append(self.parse_statement())
        self.consume("PUNCTUATION", "}")
        self.consume("PUNCTUATION", ";")
        return {
            "type": "condition",
            "condition_type": condition_type,
            "condition": condition,
            "body": body,
        }

    def parse_statement(self):
        if self.peek()[0] == "KEYWORD" and self.peek()[1] == "fprint":
            return self.parse_print()
        raise ValueError(f"Unexpected token {self.peek()}")

    def parse_print(self):
        self.consume("KEYWORD", "fprint")
        self.consume("PUNCTUATION", "(")
        value = self.consume("STRING_LITERAL")
        self.consume("PUNCTUATION", ")")
        self.consume("PUNCTUATION", ";")
        return {"type": "print", "value": value}

    def parse_assignment(self):
        var_name = self.consume("IDENTIFIER")
        self.consume("OPERATOR", "=")
        value = self.consume("NUMBER")
        self.consume("PUNCTUATION", ";")
        return {"type": "assignment", "name": var_name, "value": int(value)}

    def consume(self, expected_type, expected_value=None):
        token = self.tokens[self.pos]
        if token[0] != expected_type or (expected_value and token[1] != expected_value):
            raise ValueError(f"Expected {expected_type} {expected_value}, but got {token}")
        self.pos += 1
        return token[1]

    def peek(self):
        return self.tokens[self.pos]

# Interpreter class
class Interpreter:
    def __init__(self, ast):
        self.ast = ast
        self.variables = {}

    def execute(self):
        for statement in self.ast:
            self.execute_statement(statement)

    def execute_statement(self, statement):
        if statement["type"] == "assignment":
            self.variables[statement["name"]] = statement["value"]
        elif statement["type"] == "print":
            value = statement["value"]
            if value in self.variables:
                print(self.variables[value])
            else:
                print(value.strip('"'))
        elif statement["type"] == "condition":
            self.execute_condition(statement)

    def execute_condition(self, statement):
        if statement["condition_type"] == "mesh":
            for body_stmt in statement["body"]:
                self.execute_statement(body_stmt)
        else:
            left, operator, right = statement["condition"]
            if eval(f"{self.variables[left]} {operator} {right}"):
                for body_stmt in statement["body"]:
                    self.execute_statement(body_stmt)

        
file_path = 'constants/code.txt'

code = read_file(file_path)

tokens = lexer(code)
parser = Parser(tokens)
ast = parser.parse()

interpreter = Interpreter(ast)
interpreter.execute()