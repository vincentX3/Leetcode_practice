# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd_silly(self, head: ListNode, n: int) -> ListNode:
        count = 0
        pointer = head
        while pointer != None:
            count += 1
            pointer = pointer.next
        if count < 2:
            return None

        count -= n
        save_head = pointer = ListNode(-1)
        pointer.next = head
        while count > 0:
            count -= 1
            pointer = pointer.next
        if pointer.next.next:
            pointer.next = pointer.next.next
        else:
            pointer.next = None
        return save_head.next

    def removeNthFromEnd_dict(self, head: ListNode, n: int) -> ListNode:
        if head == None:
            return head

        list_dict = {}
        pointer = head
        no = 0
        while pointer != None:
            no += 1
            list_dict[no] = pointer
            pointer = pointer.next
        pre_index = no - n
        if pre_index == 0:
            return head.next
        else:
            pre = list_dict[pre_index]
            if pre.next.next:
                pre.next = pre.next.next
            else:
                pre.next = None
            return head

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        save_head = ListNode(-1)
        save_head.next = head
        fast_p = slow_p = save_head
        for _ in range(n):
            fast_p = fast_p.next
        while fast_p.next != None:
            fast_p = fast_p.next
            slow_p = slow_p.next
        slow_p.next = slow_p.next.next
        return save_head.next
