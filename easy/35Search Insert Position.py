from typing import List


class Solution:
    def searchInsert_seq(self, nums: List[int], target: int) -> int:
        # v1 sequence searching
        if target <= nums[0]:
            return 0
        index = 1
        length = len(nums)
        while index < length:
            if target > nums[index - 1] and target <= nums[index]:
                break
            index += 1
        return index

    def searchInsert(self, nums: List[int], target: int) -> int:
        #binary search version
        #list may contains duplicate value
        if target<=nums[0]:
            return 0
        elif target>nums[-1]:
            return len(nums)
        left,right=0,len(nums)
        index=right//2
        while True:
            if target>nums[index-1] and target<=nums[index]:
                break
            elif target>nums[index]:
                left=index
                index=(index+right)//2
            else: #target<nums[index-1]
                right=index
                index=(left+index-1)//2
        return index


input_list = [[[1, 3, 5, 6], 5], [[1, 3, 5, 6], 2], [[1, 3, 5, 6], 7], [[1, 3, 5, 6], 0]]
solution = Solution()
for Input in input_list:
    print(solution.searchInsert(Input[0], Input[1]))
