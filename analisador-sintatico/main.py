from lexico import LexicalAnalyzer
from sintatico import Parser

source_code = """
   // Programa de exemplo 5
fun getSum(a, b) {
  return a + b;
}

var sum = getSum(4, 5);

if(sum > 10) {
  print "yes";
} else {
  print "no";
}
    """

tokens = LexicalAnalyzer(source_code)
parser = Parser(tokens)
print(parser.parse())


