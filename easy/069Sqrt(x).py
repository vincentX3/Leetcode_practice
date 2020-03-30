class Solution:
    def mySqrt(self, x: int) -> int:
        # since x is non-negative and result would be truncated to integer.
        x0 = x
        while x0*x0 > x:
            x0 = (x0 + x // x0) // 2
        return int(x0)