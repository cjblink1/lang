
from proc.expression.expression import Expression
from proc.environment import Environment
from proc.value.expressed_value import ExpressedValue
from proc.value.integer import IntegerValue


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