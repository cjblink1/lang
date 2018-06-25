
from proc.expression.expression import Expression
from proc.environment import Environment

class LetExpression(Expression):

    def __init__(self, variable: str, bound_expression: Expression, body: Expression):
        self.variable = variable
        self.bound_expression = bound_expression
        self.body = body

    def string_representation(self):
        return "variable = {0}, bound-expression = {1}, body = {2)".format(self.variable, self.bound_expression, self.body)

    def evaluate(self, environment: Environment):
        bound_value = self.bound_expression.evaluate(environment)
        return self.body.evaluate(environment.extend(self.variable, bound_value))