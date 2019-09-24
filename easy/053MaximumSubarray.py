from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum, total = nums[0], 0
        for num in nums:
            total = total + num
            if total > maximum:  # maybe all numbers in list are negative
                maximum = total
            if total < 0:
                total = 0  # reset

        return maximum


