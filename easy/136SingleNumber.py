from typing import List


class Solution:
    def singleNumber_slow(self, nums: List[int]) -> int:
        temp = []
        for num in nums:
            if num in temp:
                temp.remove(num)
            else:
                temp.append(num)
        return temp[0]

    def singleNumber(self, nums: List[int]) -> int:
        # XOR
        if len(nums) < 2:
            return nums[0]
        temp = nums[0]
        for num in nums[1:]:
            temp = temp ^ num
        return temp
