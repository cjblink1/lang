
from proc.expression.expression import Expression
from proc.procedure import Procedure
from proc.environment import Environment


class CallExpression(Expression):

    def __init__(self, rator: Expression, rand: Expression):
        self.rator_exp = rator
        self.rand_exp = rand

    def string_representation(self):
        '[ CallExpression rator = {0}, rand = {1}]'.format(self.rator_exp, self.rand_exp)

    def evaluate(self, environment: Environment):
        rator: Procedure = self.rator_exp.evaluate(environment).extract()
        rand = self.rand_exp.evaluate(environment)
        return rator.apply(rand)