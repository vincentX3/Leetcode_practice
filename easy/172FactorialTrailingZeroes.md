#172. Factorial Trailing Zeroes

Given an integer n, return the number of trailing zeroes in n!.

Example 1:

> Input: 3  
Output: 0  
Explanation: 3! = 6, no trailing zero.  

Example 2:

> Input: 5  
Output: 1  
Explanation: 5! = 120, one trailing zero.  
>

Note: Your solution should be in logarithmic time complexity.
---
## Solutions
不难，思考一下尾缀0的个数满足如下公式：
$$zeroes=\sum_{i=1}^\log_5{n} {n//5^i}$$
实现方案，可递归可迭代，不过实现的差异对性能影响较大。