from antlr4 import *
from let.LETLexer import LETLexer
from let.LETParser import LETParser
from let.interpreter import run
from let.value import *
import unittest

class LETTest(unittest.TestCase):

    def test_let(self):
        input = InputStream('let y = 7 in if zero? (4) then -(55, -(x,11)) else 8')
        lexer = LETLexer(input)
        stream = CommonTokenStream(lexer)
        parser = LETParser(stream)
        tree = parser.program()
        print(tree.toStringTree(recog=parser))

    def test_integer_value(self):
        val = IntegerValue(2)
        self.assertEqual(2 , val.extract())

    def test_boolean_value(self):
        val = BooleanValue(True)
        self.assertTrue(val.extract())

    def test_none_value(self):
        self.assertRaises(ValueError, IntegerValue, None)

    def test_example1(self):
        program = 'let x = 5 in -(x,3)'
        self.assertEqual('2', run(InputStream(program)).__str__())

    def test_example2(self):
        program = '''
            let z = 5
            in let x = 3 
                in let y = - (x,1)
                    in let x = 4
                        in - (z, -(x,y))
        '''
        self.assertEqual('3', run(InputStream(program)).__str__())

    def test_example3(self):
        program = '''
            let x = 7
            in let y = 2 
                in let y = let x = - (x,1)
                            in - (x,y)
                    in - (-(x,8),y)
        '''
        self.assertEqual('-5', run(InputStream(program)).__str__())
