# 25_MergeSortedLists

## 题目描述
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

## 思路
链表基础复习。记得处理剩余有序链表.

## Solution
```python
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        p1, p2, new_list, ptr = pHead1, pHead2, ListNode(-1), None
        ptr = new_list
        while p1 and p2:
            if p1.val < p2.val:
                ptr.next = p1
                p1 = p1.next
            else:
                ptr.next = p2
                p2 = p2.next
            ptr = ptr.next
            ptr.next = None # for safety
        if p1:
            ptr.next = p1
        else:
            ptr.next = p2
        return new_list.next
```