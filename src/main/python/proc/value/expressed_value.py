class ExpressedValue(object):

    def __init__(self, val):
        if not val:
            raise ValueError("Cannot create NULL value.")

    def extract(self):
        raise NotImplementedError

    def __str__(self):
        return "{0}".format(self.extract())