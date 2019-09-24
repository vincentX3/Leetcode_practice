# 01Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the sameelement twice.
Example:
> Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

---

solution:
1. **brute force**：O(n^2)，直观。两层循环来检测每个`num`是否有match的other `num`
2. **hash**：O(n) 👆内层循环一遍时，就已经看到了全部的num。既然我们只需要有num1+num2=target，返回对应index，用空间换时间将num map to index就好
		1. two-pass：先遍历一边建立完整`hash table`
		2. one-pass：边找边建hash表


---
enumerate()👈 可巧用来建hash表
```python
hash={val:index for index, val in enumerate(nums)}
```
说明：
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。语法:
enumerate(sequence, [start=0])