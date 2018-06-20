from mockito import mock, verify
import unittest
from scanner import Scanner, IdentifierTokenMatcher, WhitespaceTokenMatcher

class ScannerTest(unittest.TestCase):

    def setUp(self):
        self.scanner = Scanner()
        self.scanner.add_token_matcher(IdentifierTokenMatcher())
        self.scanner.add_token_matcher(WhitespaceTokenMatcher())

    def test_identifier(self):
        result = self.scanner.generate_tokens('a')
        self.assertEqual([('id', 'a', '')], result)

    def test_whitespace(self):
        result = self.scanner.generate_tokens('       ')
        self.assertEqual([], result)

    def test_char_whitespace(self):
        result = self.scanner.generate_tokens('a       ')
        self.assertEqual([('id', 'a', '')], result)

    def test_whitespace_char(self):
        result = self.scanner.generate_tokens('       a')
        self.assertEqual([('id', 'a', '')], result)

    def test_whitespace_char_whitespace(self):
        result = self.scanner.generate_tokens('   a   ')
        self.assertEqual([('id', 'a', '')], result)

    def test_char_whitespace_char(self):
        result = self.scanner.generate_tokens('a a')
        self.assertEqual([('id', 'a', ''), ('id', 'a', '')], result)

# test = ScannerTest()
# test.setUp()
# test.test_char_whitespace()