# Generated from PROC.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LETParser import LETParser
else:
    from LETParser import LETParser

from let.expression import *

# This class defines a complete generic visitor for a parse tree produced by LETParser.

class LETVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LETParser#program.
    def visitProgram(self, ctx:LETParser.ProgramContext):
        return ProgramExpression(self.visit(ctx.expression()))


    # Visit a parse tree produced by LETParser#expression.
    def visitExpression(self, ctx:LETParser.ExpressionContext):
        return self.visit(ctx.children[0])


    # Visit a parse tree produced by LETParser#constant_expression.
    def visitConstant_expression(self, ctx:LETParser.Constant_expressionContext):
        return ConstantExpression(int(ctx.NUMBER().symbol.text))


    # Visit a parse tree produced by LETParser#difference_expression.
    def visitDifference_expression(self, ctx:LETParser.Difference_expressionContext):
        minuend = ctx.children[2]
        subtrahend = ctx.children[4]
        return DifferenceExpression(self.visit(minuend), self.visit(subtrahend))


    # Visit a parse tree produced by LETParser#zero_expression.
    def visitZero_expression(self, ctx:LETParser.Zero_expressionContext):
        return ZeroCheckExpression(self.visit(ctx.expression()))


    # Visit a parse tree produced by LETParser#if_expression.
    def visitIf_expression(self, ctx:LETParser.If_expressionContext):
        condition = ctx.children[1]
        consequent = ctx.children[3]
        alternative = ctx.children[5]
        return IfExpression(self.visit(condition), self.visit(consequent), self.visit(alternative))


    # Visit a parse tree produced by LETParser#variable_expression.
    def visitVariable_expression(self, ctx:LETParser.Variable_expressionContext):
        return VariableExpression(ctx.IDENTIFIER().symbol.text)


    # Visit a parse tree produced by LETParser#let_expression.
    def visitLet_expression(self, ctx:LETParser.Let_expressionContext):
        variable = ctx.IDENTIFIER().symbol.text
        bound_expression = ctx.children[3]
        body = ctx.children[5]
        return LetExpression(variable, self.visit(bound_expression), self.visit(body))



del LETParser