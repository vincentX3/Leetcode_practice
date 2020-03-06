# 06_PrintListInReversedOrder

## 题目描述
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。

## 思路
链表只能顺序输入，要求逆序输出。  
若不能改变链表结构（反转链表），显然使用**stack**或**递归**（本质上仍是stack）

## Solution
``` python
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        stack=[]
        while listNode:
            stack.append(listNode.val)
            listNode=listNode.next
        stack.reverse()
        return stack
```