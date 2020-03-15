from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_map = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'],
                     '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'],
                     '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        result = []
        for digit in list(digits):
            num = len(result)
            if num == 0:  # init
                result = phone_map[digit].copy()
            else:
                for _ in range(num):
                    prefix = result.pop(0)
                    for char in phone_map[digit]:
                        result.append(prefix + char)
        return result


class Solution2:
    # reference: by Leetcode sample.
    # using recursion and dict production. Elegant!
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        res = [""]
        self.str = digits
        self.dict1 = {"2": ["a", "b", "c"], "3": ["d", 'e', 'f'], "4": ['g', 'h', 'i'], "5": ['j', 'k', 'l'],
                      "6": ['m', 'n', 'o'], "7": ["p", 'q', 'r', 's'], "8": ['t', 'u', 'v'], "9": ['w', 'x', 'y', 'z']}
        return self.comb(0, res)

    def comb(self, i, res):
        if i == len(self.str):
            return res
        res1 = []
        while len(res) != 0:
            a = res.pop()
            b = [a + j for j in self.dict1[self.str[i]]]
            res1 += b
        return self.comb(i + 1, res1)


s = Solution()
print(s.letterCombinations('22'))
