# 22. Generate Parentheses

```
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```

## Notes

对于n个括号的排列，实质是从`0->n`建立一颗解集树。
leetcode discussion里提供了很优雅的dp思路，转述如下：
设`dp[n]`为括号数为`n`的排列解集，
有
$$
dp[n]=\sum_{i=0}^{n-1}(dp[i])dp[n-i-1]
$$
举例有：
``
s.generateParenthesis(3)
i=0,n-i-1=0 [[''], ['()'], [], []]
i=0,n-i-1=1 [[''], ['()'], ['()()'], []]
i=1,n-i-1=0 [[''], ['()'], ['()()', '(())'], []]
i=0,n-i-1=2 [[''], ['()'], ['()()', '(())'], ['()()()', '()(())']]
i=1,n-i-1=1 [[''], ['()'], ['()()', '(())'], ['()()()', '()(())', '(())()']]
i=2,n-i-1=0 [[''], ['()'], ['()()', '(())'], ['()()()', '()(())', '(())()', '(()())', '((()))']]
``
优雅的实现见代码。膜拜了。