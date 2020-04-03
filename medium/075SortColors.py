from  typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # v1 two pass use buckets
        buckets=[0,0,0]
        for num in nums:
            buckets[num]+=1
        start=0
        for i,bucket in enumerate(buckets):
            nums[start:start+bucket]=[i for _ in range(bucket)]
            start+=bucket
        return

    def sortColors_leetcode(self, nums):
        red, white, blue = 0, 0, len(nums)-1
        
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1