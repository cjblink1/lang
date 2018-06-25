
from let.environment import Environment
from let.values import *


class Expression(object):

    def __str__(self):
        return "[ " + self.__class__.__name__ + " " + self.string_representation() + " ]"

    def string_representation(self) -> str:
        raise NotImplementedError

    def evaluate(self, environment: Environment) -> ExpressedValue:
        raise NotImplementedError


class ProgramExpression(Expression):

    def __init__(self, body: Expression):
        self.body = body

    def string_representation(self):
        return "body = {0}".format(self.body)

    def evaluate(self, environment: Environment) -> ExpressedValue:
        self.body.evaluate(environment)


class ConstantExpression(Expression):

    def __init__(self, num: int):
        self.num = num

    def string_representation(self):
        return "num = {0}".format(self.num)

    def evaluate(self, environment: Environment) -> ExpressedValue:
        return IntegerValue(self.num)


class DifferenceExpression(Expression):

    def __init__(self, minuend: Expression, subtrahend: Expression):
        self.minuend_exp = minuend
        self.subtrahend_exp = subtrahend

    def string_representation(self):
        return "minuend = {0}, subtrahend = {1}".format(self.minuend_exp, self.subtrahend_exp)

    def evaluate(self, environment: Environment) -> ExpressedValue:
        min_val = self.minuend_exp.evaluate(environment)
        sub_val = self.subtrahend_exp.evaluate(environment)
        minuend = min_val.extract()
        subtrahend = sub_val.extract()
        return IntegerValue(minuend - subtrahend)


class ZeroCheckExpression(Expression):

    def __init__(self, operand: Expression):
        self.operand_exp = operand

    def string_representation(self):
        return "operand = {0}".format(self.operand_exp)

    def evaluate(self, environment: Environment) -> ExpressedValue:
        operand_val = self.operand_exp.evaluate(environment)
        operand = operand_val.extract()
        return BooleanValue(operand == 0)


class IfExpression(Expression):

    def __init__(self, condition: Expression, consequent: Expression, alternative: Expression):
        self.condition_exp = condition
        self.consequent_exp = consequent
        self.alternative_exp = alternative

    def string_representation(self):
        return "condition = {0}, consequent = {1}, alternative = {2}"\
            .format(self.condition_exp, self.consequent_exp, self.alternative_exp)

    def evaluate(self, environment: Environment):
        condition_val = self.condition_exp.evaluate(environment)
        condition = condition_val.extract()
        if condition:
            return self.consequent_exp.evaluate(environment)
        else:
            return self.alternative_exp.evaluate(environment)


class VariableExpression(Expression):

    def __init__(self, identifier: str):
        self.identifier = identifier

    def string_representation(self):
        return "identifier = {0}".format(self.identifier)

    def evaluate(self, environment: Environment):
        return environment.apply(self.identifier)


class LetExpression(Expression):

    def __init__(self, variable: str, bound_expression: Expression, body: Expression):
        self.variable = variable
        self.bound_expression = bound_expression
        self.body = body

    def string_representation(self):
        return "variable = {0}, bound-expression = {1}, body = ".format(self.variable, self.bound_expression, self.body)

    def evaluate(self, environment: Environment):
        bound_value = self.bound_expression.evaluate(environment)
        return self.body.evaluate(environment.extend(self.variable, bound_value))
