class Solution:
    def strStr_bf(self, haystack: str, needle: str) -> int:
        # O(nm) Brute-force
        if needle == '':
            return 0
        if len(haystack) < len(needle):
            return -1
        idx_h = -1
        found = False
        for idx in range(len(haystack) - len(needle) + 1):
            for idx_n in range(len(needle)):
                if haystack[idx + idx_n] != needle[idx_n]:
                    break
                else:
                    if idx_n == len(needle) - 1:
                        # matched
                        idx_h = idx
                        found = True
            if found:
                break
        return idx_h

    def strStr(self, haystack: str, needle: str) -> int:
        # O(n+m) using KMP
        if len(needle) == 0:
            return 0
        elif len(needle) == 1:
            # BF
            for i in range(len(haystack)):
                if haystack[i] == needle:
                    return i
            # not found
            return -1
        else:
            return self.KMP(haystack, needle)


    def KMP(self, haystack, needle):
        # generate next array, need O(n) time
        i, j, m, n = -1, 0, len(haystack), len(needle)
        next = [-1] * n
        while j < n - 1:
            # needle[k] stands for prefix, neelde[j] stands for postfix
            if i == -1 or needle[i] == needle[j]:
                i, j = i + 1, j + 1
                next[j] = i
            else:
                i = next[i]
        print(next)
        # check through the haystack using next, need O(m) time
        i = j = 0
        while i < m and j < n:
            if j == -1 or haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                j = next[j]
        if j == n:
            return i - j
        return -1


if __name__ == '__main__':
    s = Solution()
    tests = ['ABC ABCDAB ABCDABCDABDE','ABCDABD',"aabaaabaaac","aabaaac", "hello", "ll", "kobe", "", "mississippi", "issip", "a", "a"]
    for i in range(0, len(tests), 2):
        print(tests[i], tests[i + 1])
        print(s.strStr(tests[i], tests[i + 1]))
