# 66. Plus One
```
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
```

## Notes
题目说得不清不楚太让人疑惑了。
实际上很简单，就是输入一个元素为0-9的数组，视为一个整数，且该整数无前缀0。  
对这个整数加一后返回新数组。  
只需要考虑进位的处理即可。