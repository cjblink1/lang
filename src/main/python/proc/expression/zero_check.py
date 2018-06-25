

from proc.expression.expression import Expression
from proc.environment import Environment
from proc.value.expressed_value import ExpressedValue
from proc.value.boolean import BooleanValue


class ZeroCheckExpression(Expression):

    def __init__(self, operand: Expression):
        self.operand_exp = operand

    def string_representation(self):
        return "operand = {0}".format(self.operand_exp)

    def evaluate(self, environment: Environment) -> ExpressedValue:
        operand_val = self.operand_exp.evaluate(environment)
        operand = operand_val.extract()
        return BooleanValue(operand == 0)