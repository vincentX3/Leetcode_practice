# 19. Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Example:
```
Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.
```
Follow up:

Could you do this in one pass?

---
## Solutions:
> 单链表可通过增加`dummy_head`头指针简化操作。
1. 遍历计数，第二遍再删除：  
最直观的思路，先遍历一遍list求结点个数，再遍历删除第 *(total-n)th*个结点。
2. 字典存储：  
空间换时间，没啥特别解释的
3. 双指针先行：  
使用双指针，其中**快指针**先前进`n`个结点，而后双指针并进。  
当**快指针**指向链表末尾时，**慢指针**指向待删结点的前结点。