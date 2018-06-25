# Generated from PROC.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("]\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\6\16L\n\16\r\16\16")
        buf.write("\16M\3\17\3\17\7\17R\n\17\f\17\16\17U\13\17\3\20\6\20")
        buf.write("X\n\20\r\20\16\20Y\3\20\3\20\2\2\21\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21\3\2\6\3\2\62;\4\2C\\c|\5\2\62;C\\c|\5\2\13\f\17\17")
        buf.write("\"\"\2_\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\3!\3\2\2\2\5#\3")
        buf.write("\2\2\2\7%\3\2\2\2\t\'\3\2\2\2\13)\3\2\2\2\r/\3\2\2\2\17")
        buf.write("\62\3\2\2\2\21\67\3\2\2\2\23<\3\2\2\2\25@\3\2\2\2\27B")
        buf.write("\3\2\2\2\31E\3\2\2\2\33K\3\2\2\2\35O\3\2\2\2\37W\3\2\2")
        buf.write("\2!\"\7/\2\2\"\4\3\2\2\2#$\7*\2\2$\6\3\2\2\2%&\7.\2\2")
        buf.write("&\b\3\2\2\2\'(\7+\2\2(\n\3\2\2\2)*\7|\2\2*+\7g\2\2+,\7")
        buf.write("t\2\2,-\7q\2\2-.\7A\2\2.\f\3\2\2\2/\60\7k\2\2\60\61\7")
        buf.write("h\2\2\61\16\3\2\2\2\62\63\7v\2\2\63\64\7j\2\2\64\65\7")
        buf.write("g\2\2\65\66\7p\2\2\66\20\3\2\2\2\678\7g\2\289\7n\2\29")
        buf.write(":\7u\2\2:;\7g\2\2;\22\3\2\2\2<=\7n\2\2=>\7g\2\2>?\7v\2")
        buf.write("\2?\24\3\2\2\2@A\7?\2\2A\26\3\2\2\2BC\7k\2\2CD\7p\2\2")
        buf.write("D\30\3\2\2\2EF\7r\2\2FG\7t\2\2GH\7q\2\2HI\7e\2\2I\32\3")
        buf.write("\2\2\2JL\t\2\2\2KJ\3\2\2\2LM\3\2\2\2MK\3\2\2\2MN\3\2\2")
        buf.write("\2N\34\3\2\2\2OS\t\3\2\2PR\t\4\2\2QP\3\2\2\2RU\3\2\2\2")
        buf.write("SQ\3\2\2\2ST\3\2\2\2T\36\3\2\2\2US\3\2\2\2VX\t\5\2\2W")
        buf.write("V\3\2\2\2XY\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z[\3\2\2\2[\\\b")
        buf.write("\20\2\2\\ \3\2\2\2\6\2MSY\3\b\2\2")
        return buf.getvalue()


class PROCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    NUMBER = 13
    IDENTIFIER = 14
    WS = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'-'", "'('", "','", "')'", "'zero?'", "'if'", "'then'", "'else'", 
            "'let'", "'='", "'in'", "'proc'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "IDENTIFIER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "NUMBER", "IDENTIFIER", 
                  "WS" ]

    grammarFileName = "PROC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


