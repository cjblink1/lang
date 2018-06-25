
from proc.value.expressed_value import ExpressedValue
from proc.procedure import Procedure


class ProcedureValue(ExpressedValue):

    def __init__(self, p: Procedure):
        ExpressedValue.__init__(self, p)
        self.p = p

    def extract(self):
        return self.p