from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify array in-place instead.
        """
        zeros, real_index = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            else:
                nums[real_index] = nums[i]
                real_index += 1
        nums[real_index:] = [0 for x in range(zeros)]

        return