
import sys
from proc.PROCLexer import PROCLexer
from proc.PROCParser import PROCParser
from proc.PROCVisitor import PROCVisitor
from antlr4 import *
from proc.expression.program import ProgramExpression
from proc.environment import Environment


def scan_and_parse(input_stream: InputStream) -> ProgramExpression:
    lexer = PROCLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PROCParser(stream)
    tree = parser.program()
    visitor = PROCVisitor()
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
