from typing import List


class Solution:
    def threeSum_failed(self, nums: List[int]) -> List[List[int]]:
        # may exceeded time limit
        container, result = [], []
        if len(nums) < 3:
            return result
        nums.sort()
        pre = None
        for i, num in enumerate(nums[:-2]):
            record = {}
            record[0 - num - nums[i + 1]] = [num, nums[i + 1]]
            if num == pre:
                continue
            pre = num
            for num2 in nums[i + 2:]:
                temp = record.get(num2)
                if temp:
                    container.append(temp + [num2])
                record[0 - num - num2] = [num, num2]

        # delete duplicate
        for res in container:
            if res not in result:
                result.append(res)
        return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        index, length = 0, len(nums)
        while index + 2 < length:
            if index > 0 and nums[index] == nums[index - 1]:
                # skip same number
                index+=1
                continue
            # simplify problem as 2-sum
            aim = 0 - nums[index]
            left, right = index + 1, length - 1
            while left < right:
                if nums[left] + nums[right] < aim:
                    left += 1
                elif nums[left] + nums[right] > aim:
                    right -= 1
                else:
                    result.append([nums[index], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        #skip all the duplicates
                        left += 1
            index += 1
        return result


s = Solution()
tests = [[0, 0, 0, 0, 0], [-1, 0, 1, 2, -1, -4], [-2, 0, 1, 1, 2]]
for test in tests:
    print(s.threeSum(test))
