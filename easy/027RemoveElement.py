from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cursor=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[cursor]=nums[i]
                cursor+=1

        return cursor


