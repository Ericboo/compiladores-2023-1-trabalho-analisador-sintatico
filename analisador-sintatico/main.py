from lexico import LexicalAnalyzer

source_code = """
    int 2c = 10;
    """

lexer = LexicalAnalyzer(source_code)
for token in lexer:
    print(token)
