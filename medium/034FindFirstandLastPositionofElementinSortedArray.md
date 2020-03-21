# 34. Find First and Last Position of Element in Sorted Array
```
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```

## Notes

1. Naive solution
给定一个有序数组，自然想到直接二分查找判断元素是否存在，若存在则记录找到元素的下标，向前向后分别线性遍历找起始点。

2. Optimization
能更快吗？可以的！  
分析下二分查找时的判断情况，假设我们希望找`start_idx`，对于基础的二分查找，我们有：
```python
if nums[mid] == target:
       found_idx = mid
        break
    elif nums[mid] > target:
    right = mid - 1
    else:
    left = mid + 1
```
但事实上，当找`start_idx`时，`num[mid]` 不管等于还是大于`target`，`start_idx`都至少是`mid`或在其之前。  
因此，可以简化判断如下：
```python
if nums[mid] < target:
       left = mid + 1
    else:
        # whatever nums[mid] equal or larger than the target,
        # the starting index would be mid or smaller than mid
        right = mid
```
当`left==right`时查找收敛，若元素存在则`left`为其起始点。

3. Caution
代码小细节别掉坑里了！ **移位运算符**优先级**低于**算术运算！
```
>>> left = 0
>>> right = 5
>>> left + (right - left) >> 1
>>> 2
>>> left + (right - left) >> 1 + 1
>>> 1
>>> (left + (right - left) >> 1) + 1
>>> 3
```