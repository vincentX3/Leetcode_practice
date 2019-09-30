# 219. Contains Duplicate II

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

> Input: nums = [1,2,3,1], k =   
Output: true  

Example 2:

> Input: nums = [1,0,1,1], k = 1  
Output: true  

Example 3:

> Input: nums = [1,2,3,1,2,3], k = 2  
Output: false
---
##Solutions:
1. 排序后遍历  
构建(下标，数字)的二维列表，按照数字大小排序。遍历该列表进行比对
2. hashmap存储
涉及类似“window”扫描比对的题目，可以用hashmap保存此前遍历的结果，避免回退。