# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        '''
        start:
        o ->a ->b->...
        ^   ^
        p1  p2

        after:
        o ->b ->a ->...
        ^       ^
        p1      p2
        '''
        dummy = ListNode(-1)
        dummy.next = head
        p1 = p2 = dummy
        while p2.next and p2.next.next:
            p1, p2 = p2, p2.next
            # start swapping
            p1.next = p2.next
            p2.next = p2.next.next
            p1.next.next = p2

        return dummy.next