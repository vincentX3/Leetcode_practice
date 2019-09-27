from typing import List


class Solution:
    def majorityElement_dummy(self, nums: List[int]) -> int:
        record = {}
        for num in nums:
            if record.get(num):
                record[num] += 1
            else:
                record[num] = 1

        return max(record, key=lambda num: record[num])

    def majorityElement(self, nums):
        pair = 0
        candidate = None
        for num in nums:
            if pair == 0:
                candidate = num
                pair = 1
            else:
                if num == candidate:
                    pair += 1
                else:
                    pair -= 1
        return candidate
