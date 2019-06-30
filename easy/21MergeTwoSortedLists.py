# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head=l_merge=ListNode(0) # set a head pointer
        while l1 and l2:
            if l1.val<l2.val:
                l_merge.next=l1
                l1=l1.next
            else:
                l_merge.next=l2
                l2=l2.next
            l_merge=l_merge.next
        l_merge.next=l1 or l2

        return head.next


l1=ListNode(1)
l1.next=ListNode(2)
l2=ListNode(1)
l2.next=ListNode(3)

solution=Solution()
l_merge=solution.mergeTwoLists(l1,l2)
while l_merge!=None:
    print(l_merge.val,"->")
    l_merge=l_merge.next
