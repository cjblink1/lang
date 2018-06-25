
from proc.expression.expression import Expression
from proc.value.expressed_value import ExpressedValue
from proc.value.integer import IntegerValue
from proc.environment import Environment


class ConstantExpression(Expression):

    def __init__(self, num: int):
        self.num = num

    def string_representation(self):
        return "num = {0}".format(self.num)

    def evaluate(self, environment: Environment) -> ExpressedValue:
        return IntegerValue(self.num)