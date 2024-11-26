from compiler.tekonization_phase import lex


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
    
    def current_token(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None
    
    def eat(self, token_type):
        """Consume the current token if it matches the given token type."""
        if self.current_token() and self.current_token()[0] == token_type:
            self.pos += 1
        else:
            raise SyntaxError(f'Expected {token_type}, found {self.current_token()}')
    
    def parse(self):
        """Start parsing from the top-level."""
        return self.program()

    def program(self):
        """Parse a program (a series of statements)."""
        statements = []
        while self.current_token():
            stmt = self.statement()
            if stmt:
                statements.append(stmt)
        return statements

    def statement(self):
        """Parse statements such as functions, assignments, conditionals, etc."""
        token = self.current_token()

        # Parse function definition (fn keyword)
        if token and token[1] == 'fn':
            return self.function_definition()
        
        # Parse variable assignment
        if token and token[0] == 'IDENTIFIER':
            return self.assignment()
        
        # Parse conditionals (lo keyword)
        if token and token[1] == 'lo':
            return self.conditional()

        # Parse loops (floop keyword)
        if token and token[1] == 'floop':
            return self.loop()

        # Parse print or other statements (atl3bra keyword)
        if token and token[1] == 'atl3bra':
            return self.print_statement()
        
        return None
    
    def function_definition(self):
        """Parse function definitions (fn keyword)."""
        self.eat('KEYWORD')  # Eat 'fn'
        name = self.current_token()[1]
        self.eat('IDENTIFIER')  # Eat function name
        self.eat('DELIMITER')  # Eat '('
        
        params = self.parameters()  # Parse parameters
        
        self.eat('DELIMITER')  # Eat ')'
        self.eat('DELIMITER')  # Eat '{'
        
        body = self.statement()  # Parse the function body
        
        self.eat('DELIMITER')  # Eat '}'
        
        return ('FUNCTION_DEF', name, params, body)
    
    def parameters(self):
        """Parse function parameters."""
        params = []
        while self.current_token() and self.current_token()[0] == 'IDENTIFIER':
            param = self.current_token()[1]
            self.eat('IDENTIFIER')
            params.append(param)
            if self.current_token() and self.current_token()[0] == 'SEPARATOR':
                self.eat('SEPARATOR')
        return params
    
    def assignment(self):
        """Parse variable assignment."""
        var_name = self.current_token()[1]
        self.eat('IDENTIFIER')
        self.eat('OPERATOR')  # Eat '='
        value = self.current_token()[1]
        self.eat('NUMBER')  # Assume it's a number for simplicity
        return ('ASSIGNMENT', var_name, value)

    def conditional(self):
        """Parse conditional statements (lo keyword)."""
        self.eat('KEYWORD')  # Eat 'lo'
        condition = self.expression()
        self.eat('DELIMITER')  # Eat '{'
        body = self.statement()
        self.eat('DELIMITER')  # Eat '}'
        return ('CONDITIONAL', condition, body)
    
    def loop(self):
        """Parse loop statements (floop keyword)."""
        self.eat('KEYWORD')  # Eat 'floop'
        var_name = self.current_token()[1]
        self.eat('IDENTIFIER')  # Eat variable name
        self.eat('OPERATOR')  # Eat '='
        value = self.current_token()[1]
        self.eat('NUMBER')  # Eat value
        self.eat('OPERATOR')  # Eat '<'
        condition = self.current_token()[1]
        self.eat('NUMBER')  # Eat condition value
        self.eat('OPERATOR')  # Eat '++'
        return ('LOOP', var_name, value, condition)
    
    def expression(self):
        """Parse expressions (e.g., arithmetic or variable)."""
        if self.current_token()[0] == 'IDENTIFIER':
            return self.current_token()[1]  # Return the variable name
        elif self.current_token()[0] == 'NUMBER':
            return int(self.current_token()[1])  # Return the number
        return None
    
    def print_statement(self):
        """Parse a print statement (atl3bra keyword)."""
        self.eat('KEYWORD')  # Eat 'atl3bra'
        self.eat('DELIMITER')  # Eat '('
        value = self.expression()
        self.eat('DELIMITER')  # Eat ')'
        return ('PRINT', value)

# Example of parsing the code
code = """
fn good(){
    atl3bra("good code");
}
name = 42;
lo (x > 0) {
    atl3bra(x);
}
floop (x = 0, x < 10, x++) {
    atl3bra(x);
}
"""

tokens = lex(code)
parser = Parser(tokens)
ast = parser.parse()

print(ast)
