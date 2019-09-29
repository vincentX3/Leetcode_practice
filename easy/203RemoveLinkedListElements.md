# 203. Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

Example:

> Input:  1->2->6->3->4->5->6, val = 6  
Output: 1->2->3->4->5

---
## Solutions:
基本链表的删除操作，注意头结点的特殊处理：
1. 分类讨论
2. 前置补充伪头结点