from antlr4 import *
from array_init.ArrayLexer import ArrayLexer
from array_init.ArrayParser import ArrayParser
import unittest

class ArrayInitTests(unittest.TestCase):

    def test_array_init(self):
        input = InputStream('{99, 3, 451}')
        lexer = ArrayLexer(input)
        stream = CommonTokenStream(lexer)
        parser = ArrayParser(stream)
        tree = parser.init_exp()
        print(tree.toStringTree(recog=parser))

