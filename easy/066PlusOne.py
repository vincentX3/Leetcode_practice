class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        idx = len(digits) - 1
        while idx >= 0:
            if digits[idx] + 1 < 10:
                digits[idx] += 1
                break
            else:
                digits[idx] = 0
                idx -= 1
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits

# tests
# [1,2,3]
# [9,9,9]
# [2,9,9]