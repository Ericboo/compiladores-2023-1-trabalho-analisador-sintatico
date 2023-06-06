from lexico import LexicalAnalyzer

source_code = """
    // Programa de exemplo 3
    fun printSum(a, b) {
    print a + b;
    }

    printSum(10, 15);
    """

lexer = LexicalAnalyzer(source_code)
for token in lexer:
    print(token)
