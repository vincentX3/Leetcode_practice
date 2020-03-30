# 50. Pow(x, n)
```
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
```

## Notes
很经典了，无论作为递归还是动态规划的入门题。  
给了4种解法，逐步优化。
1. python提供的语法糖
2. 递归二分求解
3. 空间无优化的动态规划（有冗余运算）
4. 无冗余的动态规划