class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg_flag = (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0)
        ans, base, subtractor = 0, 1, abs(divisor)
        residue, abs_divisor = abs(dividend), abs(divisor)
        # start dividing by substraction
        while residue >= abs_divisor:
            if residue >= subtractor:
                residue -= subtractor
                ans += base
                subtractor <<= 1  # multiply 2
                base <<= 1
            else:
                subtractor >>= 1
                base >>= 1

        if neg_flag:
            ans = -ans

        # deal with over flow
        ans = min(ans, 2147483647) if not neg_flag else max(ans, -2147483648)

        return ans