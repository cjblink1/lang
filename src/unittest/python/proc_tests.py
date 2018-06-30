
import unittest
from proc.interpreter import run
from antlr4 import *


class ProcTests(unittest.TestCase):

    def test_proc1(self):
        program_string = '(proc (x) -(x,1) 7)'
        self.assertEqual('6', run(InputStream(program_string)).__str__())
