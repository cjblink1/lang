
class ExpressedValue(object):

    def extract(self):
        raise NotImplementedError

    def __str__(self):
        "{0}".format(self.extract())


class IntegerValue(ExpressedValue):

    def __init__(self, num: int):
        self.num = num

    def extract(self):
        return self.num


class BooleanValue(ExpressedValue):

    def __init__(self, b: bool):
        self.b = b

    def extract(self):
        return self.b