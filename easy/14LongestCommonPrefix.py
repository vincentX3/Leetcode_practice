from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs==[]:
            return ''
        prefix=strs[0]
        for str in strs[1:]:
            if len(prefix) > len(str):
                prefix=prefix[:len(str)]
            for i in range(len(prefix)):
                if prefix[i]!=str[i]:
                    prefix=prefix[:i]
                    break
        return prefix


    #👇 smart & elegant! So pythonic!
    def longestCommonPrefix2(self, m):
        if not m: return ''
        # since list of string will be sorted and retrieved min max by alphebetic order
        s1 = min(m)
        s2 = max(m)

        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]  # stop until hit the split index
        return s1

tests=[["flower","flow","flight"],["dog","racecar"],[],["aa","a"]]
solution=Solution()
for test in tests:
    print(solution.longestCommonPrefix(test))