from lexico import LexicalAnalyzer
from sintatico import Parser

source_code = """
   // Programa de exemplo 3
    fun printSum(a, b) {
    print a + b;
    }

    printSum(10, 15);
    """

tokens = LexicalAnalyzer(source_code)
parser = Parser(tokens)
print(parser.parse())


