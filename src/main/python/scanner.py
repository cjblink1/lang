from typing import List, Tuple
import re

class TokenMatcher(object):

    def matches_token(self, input: str) -> bool:
        raise NotImplementedError

    def generate_token(self, input: str) -> Tuple[str, str, str]:
        raise NotImplementedError


class IdentifierTokenMatcher(TokenMatcher):

    def matches_token(self, input: str) -> bool:
        return re.fullmatch('[a-zA-Z][a-zA-Z0-9]*', input)

    def generate_token(self, input: str) -> Tuple[str, str, str]:
        return ('id', input, '')

class WhitespaceTokenMatcher(TokenMatcher):

    def matches_token(self, input: str):
        return re.fullmatch('[ \n]+', input)

    def generate_token(self, input: str) -> Tuple[str, str, str]:
        return None

class Scanner(object):

    def __init__(self):
        self.token_matchers: List[TokenMatcher] = []
    
    def add_token_matcher(self, token_matcher: TokenMatcher):
        self.token_matchers.append(token_matcher)

    def generate_tokens(self, input: str) -> List[Tuple[str, str, str]]:
        first_token_string = self._find_first_token_string(input, 1)
        if not first_token_string:
            return []
        remaining_input = input[len(first_token_string):]
        for token_matcher in self.token_matchers:
            if token_matcher.matches_token(first_token_string):
                first_token = token_matcher.generate_token(first_token_string)
                return [first_token] + self.generate_tokens(remaining_input) if first_token else self.generate_tokens(remaining_input)

    def _find_first_token_string(self, remaining_input: str, cutoff: int) -> Tuple[str, str, str]:
        if cutoff > len(remaining_input):
            return None
        token_string_candidate = remaining_input[:cutoff]
        for token_matcher in self.token_matchers:
            if token_matcher.matches_token(token_string_candidate):
                next_candidate = self._find_first_token_string(remaining_input, cutoff+1)
                if not next_candidate:
                    return token_string_candidate
                return next_candidate
        return None





