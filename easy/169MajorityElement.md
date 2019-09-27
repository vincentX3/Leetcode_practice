# 169. Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

>Input: [3,2,3]  
Output: 3

Example 2:

> Input: [2,2,1,1,1,2,2]  
Output: 2

---
## Solutions
1. hash计数
2. 投票算法
    > reference:[投票算法](https://blog.csdn.net/u014248127/article/details/79230221)
    两两比较，存同去异。
3. 排序后取`nums[len(nums)//2]`的元素
`majority`占列表的一半有多，故有此方。（查阅ranks时看到的）