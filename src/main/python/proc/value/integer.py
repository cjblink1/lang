
from proc.value.expressed_value import ExpressedValue


class IntegerValue(ExpressedValue):

    def __init__(self, num: int):
        ExpressedValue.__init__(self, num)
        self.num = num

    def extract(self):
        return self.num