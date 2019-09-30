from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_nums = list(enumerate(nums))
        index_nums.sort(key=lambda x: x[1])  # sort by number
        for i in range(len(nums) - 1):
            if index_nums[i][1] == index_nums[i + 1][1]:
                if abs(index_nums[i][0] - index_nums[i + 1][0]) <= k:
                    return True
        return False

    def containsNearbyDuplicate_hash(self, nums: List[int], k: int) -> bool:
        hash={}
        for index,num in enumerate(nums):
            if num in hash and index-hash[num]<=k:
                return True
            else:
                hash[num]=index
        return False