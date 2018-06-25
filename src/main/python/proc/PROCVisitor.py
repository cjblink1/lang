# Generated from PROC.g4 by ANTLR 4.7.1
from antlr4 import *
from proc.expression.program import ProgramExpression
from proc.expression.constant import ConstantExpression
from proc.expression.difference import DifferenceExpression
from proc.expression.zero_check import ZeroCheckExpression
from proc.expression.variable import VariableExpression
from proc.expression.if_ import IfExpression
from proc.expression.let import LetExpression
from proc.expression.procedure import ProcedureExpression
from proc.expression.call import CallExpression
if __name__ is not None and "." in __name__:
    from .PROCParser import PROCParser
else:
    from PROCParser import PROCParser


# This class defines a complete generic visitor for a parse tree produced by PROCParser.
class PROCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LETParser#program.
    def visitProgram(self, ctx: PROCParser.ProgramContext):
        return ProgramExpression(self.visit(ctx.expression()))

    # Visit a parse tree produced by LETParser#expression.
    def visitExpression(self, ctx: PROCParser.ExpressionContext):
        return self.visit(ctx.children[0])

    # Visit a parse tree produced by LETParser#constant_expression.
    def visitConstant_expression(self, ctx: PROCParser.Constant_expressionContext):
        return ConstantExpression(int(ctx.NUMBER().symbol.text))

    # Visit a parse tree produced by LETParser#difference_expression.
    def visitDifference_expression(self, ctx: PROCParser.Difference_expressionContext):
        minuend = ctx.children[2]
        subtrahend = ctx.children[4]
        return DifferenceExpression(self.visit(minuend), self.visit(subtrahend))

    # Visit a parse tree produced by LETParser#zero_expression.
    def visitZero_expression(self, ctx: PROCParser.Zero_expressionContext):
        return ZeroCheckExpression(self.visit(ctx.expression()))

    # Visit a parse tree produced by LETParser#if_expression.
    def visitIf_expression(self, ctx: PROCParser.If_expressionContext):
        condition = ctx.children[1]
        consequent = ctx.children[3]
        alternative = ctx.children[5]
        return IfExpression(self.visit(condition), self.visit(consequent), self.visit(alternative))

    # Visit a parse tree produced by LETParser#variable_expression.
    def visitVariable_expression(self, ctx: PROCParser.Variable_expressionContext):
        return VariableExpression(ctx.IDENTIFIER().symbol.text)

    # Visit a parse tree produced by LETParser#let_expression.
    def visitLet_expression(self, ctx: PROCParser.Let_expressionContext):
        variable = ctx.IDENTIFIER().symbol.text
        bound_expression = ctx.children[3]
        body = ctx.children[5]
        return LetExpression(variable, self.visit(bound_expression), self.visit(body))


    # Visit a parse tree produced by PROCParser#procedure_expression.
    def visitProcedure_expression(self, ctx:PROCParser.Procedure_expressionContext):
        parameter = ctx.children[2]
        body = ctx.children[4]
        return ProcedureExpression(parameter.symbol.text, self.visit(body))


    # Visit a parse tree produced by PROCParser#call_expression.
    def visitCall_expression(self, ctx:PROCParser.Call_expressionContext):
        rator = ctx.children[1]
        rand = ctx.children[2]
        return CallExpression(self.visit(rator), self.visit(rand))



del PROCParser