# 2. Add Two Numbers

You are given two **non-empty** linked lists representing two non-negative integers.   
The digits are stored in **reverse** order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

>Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)  
Output: 7 -> 0 -> 8  
Explanation: 342 + 465 = 807.

---
## solution1:
基本的按位加法，注意处理进位(carry)。
链表操作注意细节，头指针和空指针小心。
个人版本见1，更优雅的版本见3

## solution2：
step1：将链表转换为实数
step2：两实数相加
step3：将和转换为逆序链表