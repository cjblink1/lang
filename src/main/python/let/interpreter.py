
import sys
from let.LETLexer import LETLexer
from let.LETParser import LETParser
from let.LETVisitor import LETVisitor
from antlr4 import *
from let.expression import *


def scan_and_parse(input_stream: InputStream) -> ProgramExpression:
    lexer = LETLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LETParser(stream)
    tree = parser.program()
    visitor = LETVisitor()
    return visitor.visit(tree)


def value_of_program(program_expression: ProgramExpression):
    return program_expression.evaluate(Environment())


def run(input_stream: InputStream):
    return value_of_program(scan_and_parse(input_stream))


def repl():
    try:
        while True:
            program = input('--> ')
            print(run(InputStream(program)))
    except KeyboardInterrupt:
        print('\n')
        sys.exit(0)


def main():
    if len(sys.argv) > 1:
        run(FileStream(sys.argv[1], 'UTF-8'))
    else:
        repl()
