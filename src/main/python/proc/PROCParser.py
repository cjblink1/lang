# Generated from PROC.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("L\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\5\3!\n\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\2\2\f\2\4\6\b\n")
        buf.write("\f\16\20\22\24\2\2\2H\2\26\3\2\2\2\4 \3\2\2\2\6\"\3\2")
        buf.write("\2\2\b$\3\2\2\2\n+\3\2\2\2\f\60\3\2\2\2\16\67\3\2\2\2")
        buf.write("\209\3\2\2\2\22@\3\2\2\2\24F\3\2\2\2\26\27\5\4\3\2\27")
        buf.write("\3\3\2\2\2\30!\5\6\4\2\31!\5\b\5\2\32!\5\n\6\2\33!\5\f")
        buf.write("\7\2\34!\5\16\b\2\35!\5\20\t\2\36!\5\22\n\2\37!\5\24\13")
        buf.write("\2 \30\3\2\2\2 \31\3\2\2\2 \32\3\2\2\2 \33\3\2\2\2 \34")
        buf.write("\3\2\2\2 \35\3\2\2\2 \36\3\2\2\2 \37\3\2\2\2!\5\3\2\2")
        buf.write("\2\"#\7\17\2\2#\7\3\2\2\2$%\7\3\2\2%&\7\4\2\2&\'\5\4\3")
        buf.write("\2\'(\7\5\2\2()\5\4\3\2)*\7\6\2\2*\t\3\2\2\2+,\7\7\2\2")
        buf.write(",-\7\4\2\2-.\5\4\3\2./\7\6\2\2/\13\3\2\2\2\60\61\7\b\2")
        buf.write("\2\61\62\5\4\3\2\62\63\7\t\2\2\63\64\5\4\3\2\64\65\7\n")
        buf.write("\2\2\65\66\5\4\3\2\66\r\3\2\2\2\678\7\20\2\28\17\3\2\2")
        buf.write("\29:\7\13\2\2:;\7\20\2\2;<\7\f\2\2<=\5\4\3\2=>\7\r\2\2")
        buf.write(">?\5\4\3\2?\21\3\2\2\2@A\7\16\2\2AB\7\4\2\2BC\7\20\2\2")
        buf.write("CD\7\6\2\2DE\5\4\3\2E\23\3\2\2\2FG\7\4\2\2GH\5\4\3\2H")
        buf.write("I\5\4\3\2IJ\7\6\2\2J\25\3\2\2\2\3 ")
        return buf.getvalue()


class PROCParser ( Parser ):

    grammarFileName = "PROC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'-'", "'('", "','", "')'", "'zero?'", 
                     "'if'", "'then'", "'else'", "'let'", "'='", "'in'", 
                     "'proc'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUMBER", "IDENTIFIER", "WS" ]

    RULE_program = 0
    RULE_expression = 1
    RULE_constant_expression = 2
    RULE_difference_expression = 3
    RULE_zero_expression = 4
    RULE_if_expression = 5
    RULE_variable_expression = 6
    RULE_let_expression = 7
    RULE_procedure_expression = 8
    RULE_call_expression = 9

    ruleNames =  [ "program", "expression", "constant_expression", "difference_expression", 
                   "zero_expression", "if_expression", "variable_expression", 
                   "let_expression", "procedure_expression", "call_expression" ]

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
    T__11=12
    NUMBER=13
    IDENTIFIER=14
    WS=15

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
            return self.getTypedRuleContext(PROCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PROCParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = PROCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
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
            return self.getTypedRuleContext(PROCParser.Constant_expressionContext,0)


        def difference_expression(self):
            return self.getTypedRuleContext(PROCParser.Difference_expressionContext,0)


        def zero_expression(self):
            return self.getTypedRuleContext(PROCParser.Zero_expressionContext,0)


        def if_expression(self):
            return self.getTypedRuleContext(PROCParser.If_expressionContext,0)


        def variable_expression(self):
            return self.getTypedRuleContext(PROCParser.Variable_expressionContext,0)


        def let_expression(self):
            return self.getTypedRuleContext(PROCParser.Let_expressionContext,0)


        def procedure_expression(self):
            return self.getTypedRuleContext(PROCParser.Procedure_expressionContext,0)


        def call_expression(self):
            return self.getTypedRuleContext(PROCParser.Call_expressionContext,0)


        def getRuleIndex(self):
            return PROCParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = PROCParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PROCParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.constant_expression()
                pass
            elif token in [PROCParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.difference_expression()
                pass
            elif token in [PROCParser.T__4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 24
                self.zero_expression()
                pass
            elif token in [PROCParser.T__5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 25
                self.if_expression()
                pass
            elif token in [PROCParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 5)
                self.state = 26
                self.variable_expression()
                pass
            elif token in [PROCParser.T__8]:
                self.enterOuterAlt(localctx, 6)
                self.state = 27
                self.let_expression()
                pass
            elif token in [PROCParser.T__11]:
                self.enterOuterAlt(localctx, 7)
                self.state = 28
                self.procedure_expression()
                pass
            elif token in [PROCParser.T__1]:
                self.enterOuterAlt(localctx, 8)
                self.state = 29
                self.call_expression()
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
            return self.getToken(PROCParser.NUMBER, 0)

        def getRuleIndex(self):
            return PROCParser.RULE_constant_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant_expression" ):
                return visitor.visitConstant_expression(self)
            else:
                return visitor.visitChildren(self)




    def constant_expression(self):

        localctx = PROCParser.Constant_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_constant_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(PROCParser.NUMBER)
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
                return self.getTypedRuleContexts(PROCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PROCParser.ExpressionContext,i)


        def getRuleIndex(self):
            return PROCParser.RULE_difference_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDifference_expression" ):
                return visitor.visitDifference_expression(self)
            else:
                return visitor.visitChildren(self)




    def difference_expression(self):

        localctx = PROCParser.Difference_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_difference_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(PROCParser.T__0)
            self.state = 35
            self.match(PROCParser.T__1)
            self.state = 36
            self.expression()
            self.state = 37
            self.match(PROCParser.T__2)
            self.state = 38
            self.expression()
            self.state = 39
            self.match(PROCParser.T__3)
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
            return self.getTypedRuleContext(PROCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PROCParser.RULE_zero_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitZero_expression" ):
                return visitor.visitZero_expression(self)
            else:
                return visitor.visitChildren(self)




    def zero_expression(self):

        localctx = PROCParser.Zero_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_zero_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(PROCParser.T__4)
            self.state = 42
            self.match(PROCParser.T__1)
            self.state = 43
            self.expression()
            self.state = 44
            self.match(PROCParser.T__3)
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
                return self.getTypedRuleContexts(PROCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PROCParser.ExpressionContext,i)


        def getRuleIndex(self):
            return PROCParser.RULE_if_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_expression" ):
                return visitor.visitIf_expression(self)
            else:
                return visitor.visitChildren(self)




    def if_expression(self):

        localctx = PROCParser.If_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_if_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(PROCParser.T__5)
            self.state = 47
            self.expression()
            self.state = 48
            self.match(PROCParser.T__6)
            self.state = 49
            self.expression()
            self.state = 50
            self.match(PROCParser.T__7)
            self.state = 51
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
            return self.getToken(PROCParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return PROCParser.RULE_variable_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_expression" ):
                return visitor.visitVariable_expression(self)
            else:
                return visitor.visitChildren(self)




    def variable_expression(self):

        localctx = PROCParser.Variable_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variable_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(PROCParser.IDENTIFIER)
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
            return self.getToken(PROCParser.IDENTIFIER, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PROCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PROCParser.ExpressionContext,i)


        def getRuleIndex(self):
            return PROCParser.RULE_let_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLet_expression" ):
                return visitor.visitLet_expression(self)
            else:
                return visitor.visitChildren(self)




    def let_expression(self):

        localctx = PROCParser.Let_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_let_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(PROCParser.T__8)
            self.state = 56
            self.match(PROCParser.IDENTIFIER)
            self.state = 57
            self.match(PROCParser.T__9)
            self.state = 58
            self.expression()
            self.state = 59
            self.match(PROCParser.T__10)
            self.state = 60
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Procedure_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PROCParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(PROCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PROCParser.RULE_procedure_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcedure_expression" ):
                return visitor.visitProcedure_expression(self)
            else:
                return visitor.visitChildren(self)




    def procedure_expression(self):

        localctx = PROCParser.Procedure_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_procedure_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(PROCParser.T__11)
            self.state = 63
            self.match(PROCParser.T__1)
            self.state = 64
            self.match(PROCParser.IDENTIFIER)
            self.state = 65
            self.match(PROCParser.T__3)
            self.state = 66
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Call_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PROCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PROCParser.ExpressionContext,i)


        def getRuleIndex(self):
            return PROCParser.RULE_call_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_expression" ):
                return visitor.visitCall_expression(self)
            else:
                return visitor.visitChildren(self)




    def call_expression(self):

        localctx = PROCParser.Call_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_call_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(PROCParser.T__1)
            self.state = 69
            self.expression()
            self.state = 70
            self.expression()
            self.state = 71
            self.match(PROCParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





