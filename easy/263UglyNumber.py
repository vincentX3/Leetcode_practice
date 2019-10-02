from typing import List


class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        while num & 1 == 0:
            num >>= 1
        divisors = [15, 5, 3]
        for divisor in divisors:
            while num % divisor == 0:
                num /= divisor
        return num == 1