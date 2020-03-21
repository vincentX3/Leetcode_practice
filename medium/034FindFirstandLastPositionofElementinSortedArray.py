from typing import List


class Solution:
    def searchRange_v1(self, nums: List[int], target: int) -> List[int]:
        # exception
        if not nums:
            return [-1, -1]
        result = [-1, -1]
        found_idx = -1
        left, right = 0, len(nums) - 1
        # binary search
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                found_idx = mid
                break
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if found_idx != -1:
            # found
            start, end = found_idx, found_idx
            # find start idx
            while start > 0 and nums[start - 1] == target:
                start -= 1
            while end < len(nums) - 1 and nums[end + 1] == target:
                end += 1
            result = [start, end]
        return result

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        result = [-1, -1]
        left, right = 0, len(nums) - 1
        # search starting idx
        while left < right:
            mid = left + ((right - left) >> 1) # bit operation's priority is lower than add
            if nums[mid] < target:
                left = mid + 1
            else:
                # whatever nums[mid] equal or larger than the target,
                # the starting index would be mid or smaller than mid
                right = mid
        if nums[left] == target:
            # found
            result[0] = left
            right = len(nums) - 1  # reset right idx
            while left < right:
                print(mid)
                mid = left + ((right - left) >> 1) + 1 # trick: add bias to jump out of loop
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid
            result[1] = right
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([5, 7, 7, 8, 8, 10], 8))

# test cases
# [5,7,7,8,8,10]
# 8
# [5,7,7,8,8,10]
# 6
# []
# 1
# [6,6,6,6,6,6]
# 6
# [1,1,1,3,4,16]
# 1
# [0,5,6,8,8,8,8]
# 8
