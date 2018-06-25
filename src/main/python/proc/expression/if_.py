
from proc.expression.expression import Expression
from proc.environment import Environment


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