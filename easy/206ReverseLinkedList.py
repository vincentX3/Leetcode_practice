# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head==None:
            return head
        stack=[]
        while head.next:
            stack.append(head)
            head=head.next
        cursor=head #treach the end
        while len(stack)>0:
            cursor.next=stack.pop()
            cursor=cursor.next
        cursor.next=None #break the loop
        return head

    def reverseList_recursive(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        end_node=self.reverseList_recursive(head.next) #recursively find the end node of the list
        head.next.next=head #reverse
        head.next=None #suspend
        return end_node

solution=Solution()
tests=[ListNode(1),ListNode(-1),None]
tests[0].next=ListNode(2)
tests[0].next.next=ListNode(3)
for test in tests:
    solution.reverseList(test)