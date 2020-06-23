# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given array = [2, 7, 11, 15], target = 9,
#
# Because array[0] + array[1] = 2 + 7 = 9,
# return [0, 1].

from typing import List

class Solution:

    #brute force Time: O(n^2)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution=[]
        for i in range(len(nums)):
            # if array[i]>target:
            #     continue
            # wrong↑ 有负数无法处理
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    solution.append(i)
                    solution.append(j)
                    return solution

    #two pass hash
    #ne
    def twoSum2(self,nums,target):
        hash={val:index for index, val in enumerate(nums)}
        for i in range(len(nums)):
            j=hash.get(target-nums[i])
            if j!=None and j!=i: #deal with target=2*num[i]
                return i,j

    #one pass hash
    def twoSum3(self,nums,target):
        hash={}
        for i in range(len(nums)):
            j=hash.get(target-nums[i])
            if j!=None:
                return j,i
            else:
                hash[nums[i]]=i


print(Solution().twoSum2([4,2,6, 11, 15],8))