from typing import List


class Solution:
    def canJump_dummy(self, nums: List[int]) -> bool:
        if not nums:
            return False
        possibility = [0 for _ in range(len(nums))]
        possibility[0] = 1
        for i, num in enumerate(nums):
            if possibility[i] == 1:  # can jump
                for j in range(1, num + 1):
                    if i + j < len(possibility):
                        possibility[i + j] = 1
                    else:
                        break
        return True if possibility[-1] else False

    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        farest, aim = 0, len(nums) - 1
        for i, num in enumerate(nums):
            if farest >= i:  # can reach here
                if i + num > farest:
                    farest = i + num
                if farest >= aim:
                    return True
            else:
                break
        return False
