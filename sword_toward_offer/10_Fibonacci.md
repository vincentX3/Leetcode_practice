# 10_Fibonacci

## 题目描述
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39

## 思路
天然的动态规划。
$$dp[n]=dp[n-1]+dp[n-2]$$

tricks：只求一次解时，用**滚动数组**

## Solution
```python
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        dp=[0,1]
        for i in range(2,n+1):
            dp.append(dp[-1]+dp[-2])
        return dp[n]
        
    def Fibonacci_loop(self,n):
        dp=[0,1]
        if n<=1:
            return dp[n]
        
        index=1
        for count in range(1,n):
            index=(index+1)%2
            dp[index]=dp[0]+dp[1]
        
        return dp[index]
```