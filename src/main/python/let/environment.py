from let.value import ExpressedValue
from typing import Dict
from copy import deepcopy


class Environment(object):

    def __init__(self, bindings: Dict[str, ExpressedValue] = {}):
        self.bindings: Dict[str, ExpressedValue] = bindings

    def apply(self, var) -> ExpressedValue:
        return self.bindings[var]

    def extend(self, var: str, val: ExpressedValue):
        new_bindings = deepcopy(self.bindings)
        new_bindings[var] = val
        return Environment(new_bindings)
