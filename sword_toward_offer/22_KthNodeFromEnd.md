# 22_KthNodeFromEnd

## 题目描述
输入一个链表，输出该链表中倒数第k个结点。

## 思路
- 单链表遍历 -> 先后指针游走。
- 单链表异常值谨慎处理。

## Solution
```python
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        lead_ptr, k_ptr = head, head
        while k > 0:
            if lead_ptr:
                lead_ptr = lead_ptr.next
                k-=1
            else:
                return None # len(list) < k
        while lead_ptr:
            k_ptr = k_ptr.next
            lead_ptr = lead_ptr.next
        
        return k_ptr
```