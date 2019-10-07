# 371. Sum of Two Integers

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

> Input: a = 1, b = 2  
Output: 3

Example 2:

> Input: a = -2, b = 3  
Output: 1
--- 

## Solutions:
1. XOR求无进位解+AND处理进位  
首先两数XOR得到每个位上相加的**非进位解**，再使用`carry`存储进位，**AND**分条件处理`carry`，更新`非进位解`。  
其中，使用`bit_mask`来进行位操作。  
然而失败了……python中对负数的处理让我不能惯常地按照**补码取反加一**来转为规定位长的正数进行计算……
    > UPDATE:
    > 学习法2设置上下界后可实现对负数的处理，不过本算法仍有致命缺陷。当两数位数相同且最高位发生进位时，无法实现最高位的进位。（循环条件问题）                                                                                                                                                                                
     不打算再修补了，法2是更好的算法。

2. 设置上下界并循环
    > reference:[answer by pushazhiniao](https://leetcode.com/problems/sum-of-two-integers/discuss/84282/Python-solution-with-no-%22%2B-*%22-completely-bit-manipulation-guaranteed)

    思路相近但更简明。**XOR**得到**非进位解**，两数**AND**并结果**左移1位**即为进位，于是循环运算直至进位为0即可。
    python对整数的动态处理解决了上下溢的风险，不过隐藏了补码机制。为了处理位运算的负数，手动**设置32-bit的上下界**。