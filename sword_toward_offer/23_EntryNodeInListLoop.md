# 23_EntryNodeInListLoop

## 题目描述
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

## 思路
1. 判断有环：**快慢指针**。若快的追上慢的，有环；否则快的指针先指向`Null`；
2. 找到环的入口：
    1. 先确定环的长度`n`；
    2. 有环的长度后让快指针先行`n`，在和慢指针同步长移动

## Solution
```python
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead:
            return None
        loop_node = self.has_loop(pHead)
        if not loop_node:
            return None
        # count the length of loop
        count, check_point = 1, loop_node
        loop_node = loop_node.next
        while loop_node != check_point:
            loop_node = loop_node.next
            count +=1
        # find the entry
        pre, entry = pHead, pHead
        while count >0:
            pre = pre.next
            count -=1
        while pre != entry:
            entry =  entry.next 
            pre = pre.next
        return entry
    
    def has_loop(self, pHead):
        fast, slow = pHead, pHead
        if not fast.next or not fast.next.next:
            return None
        else:
            fast = fast.next.next
        while fast.next and fast.next.next:
            if fast == slow:
                return fast
            fast = fast.next.next
            slow = slow.next
        return None
```