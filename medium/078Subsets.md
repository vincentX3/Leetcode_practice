# 78. Subsets

```
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
```

## Notes
求集合的幂集。
复习下概念：（from 百度百科）
> 幂集是集合的基本运算之一。由集合的所有子集构成的集合。对任何集合a，a的幂集P(a)={x|x⊆a}。在ZFC公理系统中，幂集公理保证任何集合的幂集均为集合。如P({a，b})={∅，{a}，{b}，{a，b}}.P(·)称为幂集运算。

求幂集：
1. 幂集中元素个数为`2^len(original_set)`，可以用二进制数表示，第i位为1表示选择原集合第i个元素，否则不选。
    > 表述略不严谨，集合中元素是无序的。第i位元素意指`nums[i]`  
   
    故只需产生二进制数并翻译为对应子集即可。
    
2. BFS  
   n个元素的幂集=n-1个元素的幂集+1个元素的幂集+该个元素添加到n-1个元素的幂集产生的集合
   队列产生解集树。