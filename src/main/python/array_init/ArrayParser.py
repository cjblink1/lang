# Generated from Array.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\7")
        buf.write("\26\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\2\7\2\13\n\2\f\2\16")
        buf.write("\2\16\13\2\3\2\3\2\3\3\3\3\5\3\24\n\3\3\3\2\2\4\2\4\2")
        buf.write("\2\2\25\2\6\3\2\2\2\4\23\3\2\2\2\6\7\7\3\2\2\7\f\5\4\3")
        buf.write("\2\b\t\7\4\2\2\t\13\5\4\3\2\n\b\3\2\2\2\13\16\3\2\2\2")
        buf.write("\f\n\3\2\2\2\f\r\3\2\2\2\r\17\3\2\2\2\16\f\3\2\2\2\17")
        buf.write("\20\7\5\2\2\20\3\3\2\2\2\21\24\5\2\2\2\22\24\7\6\2\2\23")
        buf.write("\21\3\2\2\2\23\22\3\2\2\2\24\5\3\2\2\2\4\f\23")
        return buf.getvalue()


class ArrayParser ( Parser ):

    grammarFileName = "Array.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "','", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INT", "WS" ]

    RULE_init_exp = 0
    RULE_value = 1

    ruleNames =  [ "init_exp", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    INT=4
    WS=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Init_expContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArrayParser.ValueContext)
            else:
                return self.getTypedRuleContext(ArrayParser.ValueContext,i)


        def getRuleIndex(self):
            return ArrayParser.RULE_init_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInit_exp" ):
                listener.enterInit_exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInit_exp" ):
                listener.exitInit_exp(self)




    def init_exp(self):

        localctx = ArrayParser.Init_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_init_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.match(ArrayParser.T__0)
            self.state = 5
            self.value()
            self.state = 10
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ArrayParser.T__1:
                self.state = 6
                self.match(ArrayParser.T__1)
                self.state = 7
                self.value()
                self.state = 12
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 13
            self.match(ArrayParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def init_exp(self):
            return self.getTypedRuleContext(ArrayParser.Init_expContext,0)


        def INT(self):
            return self.getToken(ArrayParser.INT, 0)

        def getRuleIndex(self):
            return ArrayParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = ArrayParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_value)
        try:
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ArrayParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.init_exp()
                pass
            elif token in [ArrayParser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.match(ArrayParser.INT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





