class Solution:
    def search(self, nums, target) -> int:
        # bisection search
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums) - 1
        INF_MIN, INF_MAX = -2147483648, 2147483648 - 1
        idx = -1
        while left < right:
            # no duplicate exists in the array. so the question is simplified
            mid = left + (right - left) // 2
            # degrade to real binary search
            num_mid = (nums[mid] if nums[mid] >= nums[0] else INF_MAX) if target >= nums[0] else (
                nums[mid] if nums[mid] < nums[0] else INF_MIN)
            print(mid, nums[mid], num_mid)
            if num_mid == target:
                idx = mid
                break
            elif num_mid < target:
                left = mid + 1
            else:
                right = mid - 1
        if nums[left] == target:
            idx = left
        return idx


if __name__ == '__main__':
    s = Solution()
    tests = [[[4, 5, 6, 7, 0, 1, 2], 0], [[1, 3], 3], [[3, 1], 1]]
    for test in tests:
        print(test[0], test[1])
        print(s.search(test[0], test[1]))
