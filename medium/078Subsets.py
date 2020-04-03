from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 求幂集
        # 二进制对应转换
        self.nums = nums
        power_set = []
        for i in range(2 ** len(nums)):
            power_set.append(self.get_set(i))
        return power_set

    def get_set(self, i):
        # translate the binary expression of i to subset
        trans_set = []
        for idx in range(len(self.nums)):
            if i & 1:
                trans_set.append(self.nums[idx])
            i >>= 1
        return trans_set

    def subsets_v2(self, nums: List[int]) -> List[List[int]]:
        # 求幂集
        # n个元素的幂集=n-1个元素的幂集+1个元素的幂集+该个元素添加到n-1个元素的幂集产生的集合
        power_set = [[]]
        for num in nums:
            cur_length = len(power_set)
            for i in range(cur_length):
                power_set.append(power_set[i] + [num])
        return power_set

    def subsets_v2_pythonic(self, nums: List[int]) -> List[List[int]]:
        power_set = [[]]
        for num in nums:
            power_set += [subset + [num] for subset in power_set]
        return power_set
