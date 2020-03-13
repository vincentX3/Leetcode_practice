# 24_ReverseList

## 题目描述
输入一个链表，反转链表后，输出新链表的表头。

## 思路
注意链表操作细节。基础，好好打磨。

## Solution
```python
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        # length > 1
        pre, ptr, tmp = None, pHead, None 
        while ptr.next:
            tmp = ptr.next
            ptr.next = pre
            pre, ptr = ptr, tmp
        ptr.next = pre
        return ptr
```