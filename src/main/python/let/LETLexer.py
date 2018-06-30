# Generated from LET.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("V\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\r\6\rE\n\r\r\r\16\rF\3\16\3\16\7\16K\n\16\f\16\16\16")
        buf.write("N\13\16\3\17\6\17Q\n\17\r\17\16\17R\3\17\3\17\2\2\20\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\3\2\6\3\2\62;\4\2C\\c|\5\2\62;C\\c|\5\2\13")
        buf.write("\f\17\17\"\"\2X\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\3\37\3\2\2\2\5!\3\2\2")
        buf.write("\2\7#\3\2\2\2\t%\3\2\2\2\13\'\3\2\2\2\r-\3\2\2\2\17\60")
        buf.write("\3\2\2\2\21\65\3\2\2\2\23:\3\2\2\2\25>\3\2\2\2\27@\3\2")
        buf.write("\2\2\31D\3\2\2\2\33H\3\2\2\2\35P\3\2\2\2\37 \7/\2\2 \4")
        buf.write("\3\2\2\2!\"\7*\2\2\"\6\3\2\2\2#$\7.\2\2$\b\3\2\2\2%&\7")
        buf.write("+\2\2&\n\3\2\2\2\'(\7|\2\2()\7g\2\2)*\7t\2\2*+\7q\2\2")
        buf.write("+,\7A\2\2,\f\3\2\2\2-.\7k\2\2./\7h\2\2/\16\3\2\2\2\60")
        buf.write("\61\7v\2\2\61\62\7j\2\2\62\63\7g\2\2\63\64\7p\2\2\64\20")
        buf.write("\3\2\2\2\65\66\7g\2\2\66\67\7n\2\2\678\7u\2\289\7g\2\2")
        buf.write("9\22\3\2\2\2:;\7n\2\2;<\7g\2\2<=\7v\2\2=\24\3\2\2\2>?")
        buf.write("\7?\2\2?\26\3\2\2\2@A\7k\2\2AB\7p\2\2B\30\3\2\2\2CE\t")
        buf.write("\2\2\2DC\3\2\2\2EF\3\2\2\2FD\3\2\2\2FG\3\2\2\2G\32\3\2")
        buf.write("\2\2HL\t\3\2\2IK\t\4\2\2JI\3\2\2\2KN\3\2\2\2LJ\3\2\2\2")
        buf.write("LM\3\2\2\2M\34\3\2\2\2NL\3\2\2\2OQ\t\5\2\2PO\3\2\2\2Q")
        buf.write("R\3\2\2\2RP\3\2\2\2RS\3\2\2\2ST\3\2\2\2TU\b\17\2\2U\36")
        buf.write("\3\2\2\2\6\2FLR\3\b\2\2")
        return buf.getvalue()


class LETLexer(Lexer):

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
    NUMBER = 12
    IDENTIFIER = 13
    WS = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'-'", "'('", "','", "')'", "'zero?'", "'if'", "'then'", "'else'", 
            "'let'", "'='", "'in'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "IDENTIFIER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "NUMBER", "IDENTIFIER", 
                  "WS" ]

    grammarFileName = "LET.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


