from proc.value.expressed_value import ExpressedValue

class BooleanValue(ExpressedValue):

    def __init__(self, b: bool):
        ExpressedValue.__init__(self, b)
        self.b = b

    def extract(self):
        return self.b