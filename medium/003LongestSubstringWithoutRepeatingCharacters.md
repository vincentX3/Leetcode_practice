#3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.
```
Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

---
## Solution:
使用一个**滑动窗口**来找最长子串。  
遇到重复字符时，将当前子串截取至前一个重复字符后，再拼接当前字符。如当前子串为`abcdefgh`,读入字符`d`，则更新子串为`efghd`。
由于python的*slice*特性，我们可以很*pythonic*的实现上述滑动窗口的模拟。(见代码1)  
当然，滑动窗口只需要起始和截止下标，再加个字典记录读入过的字符，也可实现。(见代码2)