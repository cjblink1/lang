
from proc.expression.expression import Expression
from proc.environment import Environment
from proc.value.expressed_value import ExpressedValue


class ProgramExpression(Expression):

    def __init__(self, body: Expression):
        self.body = body

    def string_representation(self):
        return "body = {0}".format(self.body)

    def evaluate(self, environment: Environment) -> ExpressedValue:
        return self.body.evaluate(environment)
