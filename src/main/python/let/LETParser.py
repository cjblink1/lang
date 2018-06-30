# Generated from LET.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write(";\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3\33\n")
        buf.write("\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\2\2\n\2\4\6\b\n\f\16\20\2\2\2\67\2")
        buf.write("\22\3\2\2\2\4\32\3\2\2\2\6\34\3\2\2\2\b\36\3\2\2\2\n%")
        buf.write("\3\2\2\2\f*\3\2\2\2\16\61\3\2\2\2\20\63\3\2\2\2\22\23")
        buf.write("\5\4\3\2\23\3\3\2\2\2\24\33\5\6\4\2\25\33\5\b\5\2\26\33")
        buf.write("\5\n\6\2\27\33\5\f\7\2\30\33\5\16\b\2\31\33\5\20\t\2\32")
        buf.write("\24\3\2\2\2\32\25\3\2\2\2\32\26\3\2\2\2\32\27\3\2\2\2")
        buf.write("\32\30\3\2\2\2\32\31\3\2\2\2\33\5\3\2\2\2\34\35\7\16\2")
        buf.write("\2\35\7\3\2\2\2\36\37\7\3\2\2\37 \7\4\2\2 !\5\4\3\2!\"")
        buf.write("\7\5\2\2\"#\5\4\3\2#$\7\6\2\2$\t\3\2\2\2%&\7\7\2\2&\'")
        buf.write("\7\4\2\2\'(\5\4\3\2()\7\6\2\2)\13\3\2\2\2*+\7\b\2\2+,")
        buf.write("\5\4\3\2,-\7\t\2\2-.\5\4\3\2./\7\n\2\2/\60\5\4\3\2\60")
        buf.write("\r\3\2\2\2\61\62\7\17\2\2\62\17\3\2\2\2\63\64\7\13\2\2")
        buf.write("\64\65\7\17\2\2\65\66\7\f\2\2\66\67\5\4\3\2\678\7\r\2")
        buf.write("\289\5\4\3\29\21\3\2\2\2\3\32")
        return buf.getvalue()


class LETParser ( Parser ):

    grammarFileName = "LET.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'-'", "'('", "','", "')'", "'zero?'", 
                     "'if'", "'then'", "'else'", "'let'", "'='", "'in'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUMBER", "IDENTIFIER", "WS" ]

    RULE_program = 0
    RULE_expression = 1
    RULE_constant_expression = 2
    RULE_difference_expression = 3
    RULE_zero_expression = 4
    RULE_if_expression = 5
    RULE_variable_expression = 6
    RULE_let_expression = 7

    ruleNames =  [ "program", "expression", "constant_expression", "difference_expression", 
                   "zero_expression", "if_expression", "variable_expression", 
                   "let_expression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    NUMBER=12
    IDENTIFIER=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(LETParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LETParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = LETParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constant_expression(self):
            return self.getTypedRuleContext(LETParser.Constant_expressionContext,0)


        def difference_expression(self):
            return self.getTypedRuleContext(LETParser.Difference_expressionContext,0)


        def zero_expression(self):
            return self.getTypedRuleContext(LETParser.Zero_expressionContext,0)


        def if_expression(self):
            return self.getTypedRuleContext(LETParser.If_expressionContext,0)


        def variable_expression(self):
            return self.getTypedRuleContext(LETParser.Variable_expressionContext,0)


        def let_expression(self):
            return self.getTypedRuleContext(LETParser.Let_expressionContext,0)


        def getRuleIndex(self):
            return LETParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = LETParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        try:
            self.state = 24
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LETParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.constant_expression()
                pass
            elif token in [LETParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.difference_expression()
                pass
            elif token in [LETParser.T__4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 20
                self.zero_expression()
                pass
            elif token in [LETParser.T__5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 21
                self.if_expression()
                pass
            elif token in [LETParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 5)
                self.state = 22
                self.variable_expression()
                pass
            elif token in [LETParser.T__8]:
                self.enterOuterAlt(localctx, 6)
                self.state = 23
                self.let_expression()
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

    class Constant_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(LETParser.NUMBER, 0)

        def getRuleIndex(self):
            return LETParser.RULE_constant_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant_expression" ):
                return visitor.visitConstant_expression(self)
            else:
                return visitor.visitChildren(self)




    def constant_expression(self):

        localctx = LETParser.Constant_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_constant_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(LETParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Difference_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LETParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LETParser.ExpressionContext,i)


        def getRuleIndex(self):
            return LETParser.RULE_difference_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDifference_expression" ):
                return visitor.visitDifference_expression(self)
            else:
                return visitor.visitChildren(self)




    def difference_expression(self):

        localctx = LETParser.Difference_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_difference_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(LETParser.T__0)
            self.state = 29
            self.match(LETParser.T__1)
            self.state = 30
            self.expression()
            self.state = 31
            self.match(LETParser.T__2)
            self.state = 32
            self.expression()
            self.state = 33
            self.match(LETParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Zero_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(LETParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LETParser.RULE_zero_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitZero_expression" ):
                return visitor.visitZero_expression(self)
            else:
                return visitor.visitChildren(self)




    def zero_expression(self):

        localctx = LETParser.Zero_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_zero_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(LETParser.T__4)
            self.state = 36
            self.match(LETParser.T__1)
            self.state = 37
            self.expression()
            self.state = 38
            self.match(LETParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class If_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LETParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LETParser.ExpressionContext,i)


        def getRuleIndex(self):
            return LETParser.RULE_if_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_expression" ):
                return visitor.visitIf_expression(self)
            else:
                return visitor.visitChildren(self)




    def if_expression(self):

        localctx = LETParser.If_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_if_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(LETParser.T__5)
            self.state = 41
            self.expression()
            self.state = 42
            self.match(LETParser.T__6)
            self.state = 43
            self.expression()
            self.state = 44
            self.match(LETParser.T__7)
            self.state = 45
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Variable_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(LETParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return LETParser.RULE_variable_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_expression" ):
                return visitor.visitVariable_expression(self)
            else:
                return visitor.visitChildren(self)




    def variable_expression(self):

        localctx = LETParser.Variable_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variable_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(LETParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Let_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(LETParser.IDENTIFIER, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LETParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LETParser.ExpressionContext,i)


        def getRuleIndex(self):
            return LETParser.RULE_let_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLet_expression" ):
                return visitor.visitLet_expression(self)
            else:
                return visitor.visitChildren(self)




    def let_expression(self):

        localctx = LETParser.Let_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_let_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(LETParser.T__8)
            self.state = 50
            self.match(LETParser.IDENTIFIER)
            self.state = 51
            self.match(LETParser.T__9)
            self.state = 52
            self.expression()
            self.state = 53
            self.match(LETParser.T__10)
            self.state = 54
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





