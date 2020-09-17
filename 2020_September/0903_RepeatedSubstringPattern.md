# Repeated Substring Pattern

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

 

**Example 1:**

```
Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
```

**Example 2:**

```
Input: "aba"
Output: False
```

**Example 3:**

```
Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
```



# Solution

1. Brute-force. Compare all possible substrings.

```python
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s)<2:
            return False
        
        def has_substring(pattern):
            if len(s) % pattern != 0:
                return False
            for idx in range(pattern,len(s)-pattern+1,pattern):
                if s[:pattern] != s[idx:idx+pattern]:
                    return False
            return True
        
        pattern = 1
        while pattern < len(s):
            if has_substring(pattern):
                return True
            pattern += 1
        
        return False
```

2. Brilliant idea! [From rsrs3, see here](https://leetcode.com/problems/repeated-substring-pattern/discuss/94334/easy-python-solution-with-explaination)

   `return s in (s+s)[1:-1]`

   Brief explanation:

   Assume `s` has repeated substring `sub_s`, which means it **at least** has **two** part of same string. ( e.g. `abcabc` has two `abc`).

   What's more, `s[0]` would be the first letter of `sub_s` and `s[-1]` would be the last letter.

   We construct `double_s = s+s` (e.g. `abcabcabcabc`), it would at least has 4 `sub_s`. Then we remove `double_s[0], double_s[-1]` to destroy the first and the last `sub_s`. Now we have at least *two* `sub_s` and it's concated, which means it could form `s`.

   Like,

   ```
   abcabc
   _bcabcabcab_
   👆having:
   _bc abcabc ab_
   ```

   

   If `s` doesn't have `sub_s`, above relation could not establish.

 