
from proc.expression.expression import Expression
from proc.environment import Environment
from proc.procedure import Procedure
from proc.value.procedure import ProcedureValue


class ProcedureExpression(Expression):

    def __init__(self, parameter: str, body: Expression):
        self.parameter = parameter
        self.body = body

    def string_representation(self):
        return "parameter = {0}, body = {1}".format(self.parameter, self.body)

    def evaluate(self, environment: Environment):
        return ProcedureValue(Procedure(self.parameter, self.body, environment))
