# 29. Divide Two Integers
```
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = truncate(3) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = truncate(-2) = 3.
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
```

## Notes

无法使用`乘、除、取模`后，我们可以执行的运算就只剩`加、减、位运算`了。  
最直觉的解法，即是不断用被除数减去除数，把除法退化为减法。但考虑到`被除数>>除数`时，算法时间效率极低，需优化。  

结合`位运算`，每次减去`2n*被除数`! 比如，`被除数=2`，则依次尝试用`2，4，8……`来做减数。

注意细节：
- 正负号处理
- overflow 处理