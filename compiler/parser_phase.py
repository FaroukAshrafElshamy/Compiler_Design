from tokenization_phase import lexer, read_file
import json

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        statements = []
        while self.pos < len(self.tokens):
            statements.append(self.statement())
        return {"<program>": statements}

    def statement(self):
        if self.match('IDENTIFIER'):
            return {"<variable_declaration>": self.variable_declaration()}
        elif self.match('KEYWORD', 'if'):
            return {"<condition_statement>": self.condition_statement()}

    def variable_declaration(self):
        identifier = self.consume('IDENTIFIER')
        self.consume('OPERATOR', '=')
        expression = self.expression()
        return {"<identifier>": identifier, "<expression>": expression}

    def condition_statement(self):
        self.consume('KEYWORD', 'if')
        self.consume('PUNCTUATION', '(')
        condition = self.condition()
        self.consume('PUNCTUATION', ')')
        self.consume('PUNCTUATION', ':')
        truee = self.statement()
        if self.match('KEYWORD', 'else'):
            self.consume('KEYWORD', 'else')
            self.consume('PUNCTUATION', ':')
            falsee = self.statement()
            return {"<if_statment>": condition, "<true>": truee, "<false>": falsee}
        return {"<if_statment>": condition, "<true>": truee}

    def condition(self):
        left = self.expression()
        operator = self.consume('OPERATOR')
        right = self.expression()
        return {"<condition>": {"<left>": left, "<operator>": operator, "<right>": right}}

    def expression(self):
        if self.match('IDENTIFIER'):
            return {"<identifier>": self.consume('IDENTIFIER')}
        elif self.match('NUMBER'):
            return {"<literal>": self.consume('NUMBER')}
        elif self.match('STRING_LITERAL'):
            return {"<literal>": self.consume('STRING_LITERAL')}

    def match(self, kind, value=None):
        if self.pos >= len(self.tokens):
            return False
        token_kind, token_value = self.tokens[self.pos]
        # print("matching", kind, value, token_kind, token_value)
        return token_kind == kind and (value is None or token_value == value)

    def consume(self, kind, value=None):
        if self.match(kind, value):
            token = self.tokens[self.pos]
            # print("%s: %s" % (kind, value))
            self.pos += 1
            return token[1]

        
file_path = './constants/code.txt'

code = read_file(file_path)

tokens = lexer(code)
parser = Parser(tokens)
# print(parser.tokens)
parse_tree = parser.parse()
# print(parse_tree)


json_object = json.dumps(parse_tree, indent=2)
print(json_object)
# with open("ParseTree.json", "w") as outfile:
#     outfile.write(json_object)