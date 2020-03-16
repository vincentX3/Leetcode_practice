# 33. Search in Rotated Sorted Array

```
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

## Notes
很有趣的一题，可以对比《剑指offer》的第11题一起做。  
题目弱化了要求，list中无重复数字。我们要实现$O(logN)$的时间复杂度，实际上是要实现**变形的二分查找**。  

为帮助理解，不妨设
$$L=[A,B],A={a_1,a_2,...,a_n},B={b_1,_b_2,..,b_m}, A<B, a_i<a_j if i<j, same as b$$  
现在我们有$L'=[B,A],target = x$，不妨设$target$存在且$target\belong{A}$。  
对于二分查找中取得的中值$mid$，若$mid\belong{B}$，即落在另一有序片段，不属于$target$存在的有序段$A$，则对于二分查找的边界而言$mid=INF_MIN$，  
同理，若$target\belong{B}$而$mid\belong{A}$，，则$mid=INF_MAX$。  
由此，退化为普通的有序无重复数组二分查找。