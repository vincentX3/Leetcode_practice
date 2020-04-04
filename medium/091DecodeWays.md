# 91. Decode Ways
```
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
```

## Notes

分析题目，len(s)=n 的数字串，不会受 n+x 长的字符串干扰，只与前n个数字有关，即可用动态规划求解。  
定义动态规划数组`dp[n]`，设`dp[i]`为长为`n`的数字串，能解码字母串的个数。
依照题意，数字可解码的区间为[1,26]，打打草稿画画图我们可以发现：
```python
if 0 < dp[i-1:i+1] <=26:
    dp[i]=dp[i-1]+dp[i-2]
eles:
    dp[i]=dp[i-1]
```
即是，第i位可解码的字母串个数，首先，其本身可以单独解码为一个字母，此外再考虑，它是否能和第i-1位数字组成字母。  

**就这样吗？**  
- 数字中的**0**要处理！  
`s[i]=='0'`时，若其能和第i-1位组成合法数字串，则可解码，否则直接返回0。  
当其合法时，`dp[i]=dp[i-2]`。

- dp数组初始化检查处理

以上，即为个人版本的dp。相当不优雅。

---

看下leetcode中的[求解吧](https://leetcode.com/problems/decode-ways/discuss/253018/Python%3A-Easy-to-understand-explanation-bottom-up-dynamic-programming)！  
```python
# dp formula
# One step jump
if 0 < int(s[i-1:i]) <= 9:    #(2)
	dp[i] += dp[i - 1]
# Two step jump
if 10 <= int(s[i-2:i]) <= 26: #(3)
	dp[i] += dp[i - 2]
```