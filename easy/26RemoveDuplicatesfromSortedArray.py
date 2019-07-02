from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        detection={}
        i,length=0,len(nums)
        while i<length:
            if nums[i] in detection:
                nums.remove(nums[i])
                length-=1
            else:
                detection[nums[i]] = 1
                i+=1
        return length

    def removeDuplicates2(self, nums):
        if not nums:
            return 0

        pointer = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[pointer]:
                pointer += 1
                nums[pointer] = nums[i]

        return pointer + 1

nums=[0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates2(nums))
print(nums)
