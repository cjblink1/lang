
from proc.environment import Environment
from proc.value.expressed_value import ExpressedValue


class Expression(object):

    def __str__(self):
        return "[ " + self.__class__.__name__ + " " + self.string_representation() + " ]"

    def string_representation(self) -> str:
        raise NotImplementedError

    def evaluate(self, environment: Environment) -> ExpressedValue:
        raise NotImplementedError