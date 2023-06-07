import re
from lexico import LexicalAnalyzer

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0
        self.current_token = self.tokens[0]

    def parse(self):
        program = self.program()
        if self.current_token[0] != 'EOF':
            self.error("Unexpected token. Expected 'EOF'.")
        return program

    def program(self):
        declarations = []
        while self.current_token[0] != 'EOF':
            declarations.append(self.declaration())
        return declarations

    def declaration(self):
        if self.current_token[0] == 'KEYWORD' and self.current_token[1] == 'fun':
            return self.fun_decl()
        elif self.current_token[0] == 'KEYWORD' and self.current_token[1] == 'var':
            return self.var_decl()
        else:
            return self.statement()

    def match(self, expected_token):
        if self.current_token[0] == expected_token[0]:
            token = self.current_token
            self.advance()
            return token[1]
        else:
            self.error(f"Unexpected token. Expected {expected_token} but got {self.current_token}.")

    def next(self):
        self.current_token_index += 1
        if self.current_token_index < len(self.tokens):
            self.current_token = self.tokens[self.current_token_index]

    def error(self, message):
        raise SyntaxError(message)

   
  