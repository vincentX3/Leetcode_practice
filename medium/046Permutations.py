from typing import List


class Solution:
    def permute_v1(self, nums: List[int]) -> List[List[int]]:
        # insert a num to  n-1 permutation to get n permutation
        # use a queue
        self.ans = []
        if nums:
            self.ans.append([nums.pop()])
            self.get_permutation(nums)
        return self.ans

    def get_permutation_v1(self, nums):
        while len(nums) != 0:
            num = nums.pop()
            print(num, nums, self.ans)
            cur_length = len(self.ans)
            for _ in range(cur_length):
                temp = self.ans.pop(0)
                for i in range(len(temp) + 1):
                    new_temp = temp.copy()
                    new_temp.insert(i, num)
                    self.ans.append(new_temp)
        return

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        if nums:
            self.get_permutation(nums, 0)
        return self.ans

    def get_permutation(self, nums, cur):
        print(cur, nums)
        if cur == len(nums) - 1:
            self.ans.append(nums.copy())  # remember use copy()
        else:
            for i in range(cur, len(nums)):
                nums[cur], nums[i] = nums[i], nums[cur]
                self.get_permutation(nums, cur + 1)
                # reset
                nums[cur], nums[i] = nums[i], nums[cur]


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))
