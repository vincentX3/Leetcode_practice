class Solution:
    def myAtoi(self, str: str) -> int:
        # remove whitespace
        str = str.strip()
        # print(str)
        if len(str) == 0:  # empty string
            return 0

        idx, count = 0, 0,
        neg_flag = False
        INF_MAX, INF_MIN = 2 ** 31 - 1, -2 ** 31

        if str[idx] == '-':
            neg_flag = True
            idx += 1
        elif str[idx] < '0' or str[idx] > '9':
            if str[idx] != '+':
                # non-numerical char
                return 0
            else:
                idx += 1  # pass the '+'

        # has numerical chars
        while idx < len(str) and str[idx] >= '0' and str[idx] <= '9':
            count = count * 10 + int(str[idx])
            idx += 1

        if neg_flag:
            count *= -1

        if count < INF_MIN:
            return INF_MIN
        elif count > INF_MAX:
            return INF_MAX
        else:
            return count


class Solution2:
    # from Leetcode sample, much more Pythonic!
    def myAtoi(self, str: str) -> int:
        num = ""
        for char in str:
            if num != "" and char in " +-":
                break
            if char in '1234567890-+':
                num += char
            elif char != " ":
                break

        if num in "+-":
            return 0
        else:
            return min(max(int(num), -2 ** 31), 2 ** 31 - 1)

if __name__ == '__main__':
    s = Solution()
    tests = ["  42", "", "foo 123", "+24mamba", "-91283472332", "91283472332"]
    for test in tests:
        print(s.myAtoi(test))
