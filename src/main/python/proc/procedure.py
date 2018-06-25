
from proc.expression.expression import Expression
from proc.environment import Environment
from proc.value.expressed_value import ExpressedValue


class Procedure(object):

    def __init__(self, parameter: str, body: Expression, saved_environment: Environment):
        self.parameter = parameter
        self.body = body
        self.saved_environment = saved_environment

    def apply(self, expressed_value: ExpressedValue):
        return self.body.evaluate(self.saved_environment.extend(self.parameter, expressed_value))

    def __str__(self):
        return "[Procedure parameter = {0}, body = {1}]".format(self.parameter, self.body)










