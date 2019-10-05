# 349. Intersection of Two Arrays

Given two arrays, write a function to compute their intersection.

Example 1:

> Input: nums1 = [1,2,2,1], nums2 = [2,2]  
Output: [2]

Example 2:

> Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]  
Output: [9,4]

Note:

Each element in the result must be unique.
The result can be in any order.

---
## Solutions:
1. built-in set
使用python内置的集合类型，求交集
2. hashtable
使用hash对其中一个list去重，用第二个list元素查找hash。本质上依旧是构建集合。
    > 关于集合的数据结构，还有树形的并查集。略微繁琐，此处未自行实现
3. 排序后合并
类似*merge sort*的思路，首先对两list各自排序，然后游标遍历比较元素。只不过把原本的两list比大小合并，变成了找等值元素的过程。                                                               