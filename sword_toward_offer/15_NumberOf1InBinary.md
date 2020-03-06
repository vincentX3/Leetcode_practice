# 15_NumberOf1InBinary

## 题目描述
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

## 思路
移位。注意负数的处理。

## Solution
``` python
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        for _ in range(32):
            count += n & 1
            n>>=1
            if n ==0:
                break
        return count
```