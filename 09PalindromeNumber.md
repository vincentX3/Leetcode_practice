# 9. Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

> Input: 121
Output: true

Example 2:

> Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

> Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

---
### solution
1. tricky one, convert int to str
    > Python强大的**切片**功能能在一行内完成字符串的反转

2. 反转一半
   
   根据 leetcode's solution 实现。算法思想：
   
   若是回文数，则其后半段和前半段相同。
   
    我们只需提取数的一半并进行比较，而不用得到完整反转后的数再做比较。

    >此思路规避了完整反转后数上溢的风险👈尽管python不会
    
    > P.S.: **Edge Detection**：先将负数和尾数为0的情况排除掉。