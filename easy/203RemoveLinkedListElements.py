from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
                return head
        while head.val==val:
            head=head.next
            if head == None:
                return head
        pre,cursor=head,head.next
        while cursor:
            if cursor.val==val:
                pre.next=cursor.next
                cursor=cursor.next
            else:
                pre,cursor=cursor,cursor.next
        return head

    def removeElements_addhead(self, head: ListNode, val: int) -> ListNode:
        pre=fake_head=ListNode(-1)
        pre.next,cursor=head,head
        while cursor:
            if cursor.val==val:
                pre.next=cursor.next
                cursor=cursor.next
            else:
                pre,cursor=cursor,cursor.next
        return fake_head.next