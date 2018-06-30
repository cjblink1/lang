
class ExpressedValue(object):

    def __init__(self, val):
        if not val:
            raise ValueError("Cannot create NULL value.")

    def extract(self):
        raise NotImplementedError

    def __str__(self):
        return "{0}".format(self.extract())


class IntegerValue(ExpressedValue):

    def __init__(self, num: int):
        ExpressedValue.__init__(self, num)
        self.num = num

    def extract(self):
        return self.num


class BooleanValue(ExpressedValue):

    def __init__(self, b: bool):
        ExpressedValue.__init__(self, b)
        self.b = b

    def extract(self):
        return self.b
