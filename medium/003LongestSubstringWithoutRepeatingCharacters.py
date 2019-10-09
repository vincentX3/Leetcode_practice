class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        aim, max_len = '', 0
        for char in s:
            if char not in aim:
                aim += char
            else:#repeated
                aim = aim[aim.rfind(char) + 1:] + char
            max_len = max(len(aim),max_len)

        return max_len

    def lengthOfLongestSubstring2(self, s):
        #from leetcode @agave
        last, res, st = {}, 0, 0
        for i, v in enumerate(s):
            if v not in last or last[v] < st:
                res = max(res, i - st + 1)
            else:
                st = last[v] + 1
            last[v] = i
        return res