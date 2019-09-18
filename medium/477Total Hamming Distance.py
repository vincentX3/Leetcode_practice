from typing import List


class Solution:
    def totalHammingDistance_exceed_time_limit(self, nums: List[int]) -> int:
        # O(n^2) time, O(1) space
        total = 0
        for i, num in enumerate(nums):
            for rest in nums[i + 1:]:
                total += bin(num ^ rest).count('1')
                # print(total, num, rest)
        return total

    def totalHammingDistance(self, nums: List[int]) -> int:
        # inspired by Discuss, O(32*n) time, use bit shifting
        if len(nums)==0:
            return 0
        total = 0
        n=len(nums)
        max_len = len(bin(max(nums))) - 2  # the return str contains '0b' at head
        for shift in range(max_len):
            bit_count = 0
            for num in nums:
                bit_count += num >> shift & 1 # use '1' as a mask
            total += bit_count * (n - bit_count)

        return total


nums_list = [[4, 14, 2], [], [1, 8, 16, 64, 128]]
solution = Solution()
for nums in nums_list:
    print(solution.totalHammingDistance(nums),'\n')
