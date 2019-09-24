import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_char = re.sub(r'[^\w]', '', s).lower()
        if s_char == s_char[::-1]:
            return True
        else:
            return False
