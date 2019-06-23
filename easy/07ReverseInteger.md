# 7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
> Input: 123
> Output: 321

Example 2:
> Input: -123
Output: -321

Example 3:

> Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

---

### solution
1. 除+模循环
2. 将x视为字符串，使用python内建的`reversed()`对字符串反转。

要点：
> 1. 负数的处理
> 2. 尽管Python不会overflow，但为满足题意，return前对$>2^{31}$进行检测。