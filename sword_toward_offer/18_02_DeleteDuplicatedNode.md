# 18_02_DeleteDuplicatedNode
## 题目描述
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

## 思路
先确定测试用例，尤其注意头节点也被删去的情况。  
使用**伪头节点**方便处理。 
链表基本删除操作复习。

## Solution
```python
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:
            return None
        pre = ListNode(-9999)
        pre.next = pHead
        cur_val = pHead.val
        ptr, fake_head = pHead, pre
        flag = False
        while ptr:
            while ptr.next and ptr.next.val == cur_val:
                flag = True
                ptr.next = ptr.next.next # remove duplicate
            if flag:
                ptr = ptr.next
                pre.next = ptr
            else:
                pre = ptr
                ptr = ptr.next
            flag = False
            if ptr:
                cur_val = ptr.val
        return fake_head.next
            
# test
# _
# 1->
# 2->2->
# 1->1->1->2->
# 1->2->3->3->4->4->5
```