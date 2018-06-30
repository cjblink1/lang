from antlr4 import *
from hello.HelloLexer import HelloLexer
from hello.HelloParser import HelloParser
import unittest


class HelloTests(unittest.TestCase):

    def test_hello(self):
        input = InputStream('hello world')
        lexer = HelloLexer(input)
        stream = CommonTokenStream(lexer)
        parser = HelloParser(stream)
        tree = parser.r()
        print(tree.toStringTree(recog=parser))