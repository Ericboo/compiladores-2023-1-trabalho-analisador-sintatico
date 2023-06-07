from lexico import LexicalAnalyzer
from sintatico import Parser

source_code = """
    // Programa de exemplo 2
    var a = 2;

    while (a < 10) {
    print a;
    a = a + 1;
    }
"""

tokens = LexicalAnalyzer(source_code)
parser = Parser(tokens)
print(parser.parse())


