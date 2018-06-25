
from proc.expression.expression import Expression
from proc.environment import Environment


class VariableExpression(Expression):

    def __init__(self, identifier: str):
        self.identifier = identifier

    def string_representation(self):
        return "identifier = {0}".format(self.identifier)

    def evaluate(self, environment: Environment):
        return environment.apply(self.identifier)