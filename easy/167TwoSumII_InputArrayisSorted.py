from typing import List

from bisect import bisect_left


class Solution:
    def twoSum_dummy(self, numbers: List[int], target: int) -> List[int]:
        for index, num in enumerate(numbers):
            try:
                index2 = numbers.index(target - num, index + 1)
                return [index + 1, index2 + 1]
            except ValueError:
                pass

    def twoSum_binary_search(self, numbers: List[int], target: int) -> List[int]:
        for index, num in enumerate(numbers):
            index2 = self.index(numbers, target - num, index + 1)
            if index2:
                return [index + 1, index2 + 1]
            else:
                pass

    def index(self, a, x, begin):
        'Locate the leftmost value exactly equal to x'
        i = bisect_left(a, x, begin)
        if i != len(a) and a[i] == x:
            return i
        else:
            return None

    def twoSum_robust(self, numbers: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(numbers)):
            j = hash.get(target - numbers[i])
            if j != None:
                return [j + 1, i + 1]
            else:
                hash[numbers[i]] = i

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointer
        left, right = 0, len(numbers) - 1
        while True:  # as there is always a solution
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left + 1, right + 1]
