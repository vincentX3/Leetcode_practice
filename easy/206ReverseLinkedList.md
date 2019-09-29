# 206. Reverse Linked List

Reverse a singly linked list.

Example:

> Input: 1->2->3->4->5->NULL  
Output: 5->4->3->2->1->NULL  

Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

---
## Solutions:
1. stack
栈实现是简单的，将末尾前的全部节点依次入栈，再依次pop出并翻转指针即可
2. recursion
python实现recursion有点tricky，我们用递归是为了寻找到**尾节点**。  
注意，我们没有像`Java`一样使用`static`来存储尾节点，因而为了最后能返回正确的头结点（也即是翻转前的尾节点），
我们只能一直`return`它。