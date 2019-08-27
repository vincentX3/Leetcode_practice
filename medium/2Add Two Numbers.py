# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        add = 0
        head = ListNode(0)
        pointer = head
        while l1 != None and l2 != None:
            temp = l1.val + l2.val + add
            pointer.next, add = self.addition(temp)
            l1 = l1.next
            l2 = l2.next
            pointer = pointer.next
        if l1 != None:
            while (add != 0):
                if (l1 == None):
                    pointer.next = ListNode(1)  # because add still equal to 1
                    pointer = pointer.next
                    break
                pointer.next, add = self.addition(l1.val + add)
                pointer = pointer.next
                l1 = l1.next
            pointer.next = l1
        else:
            while (add != 0):
                if (l2 == None):
                    pointer.next = ListNode(1)  # because add still equal to 1
                    pointer = pointer.next
                    break
                pointer.next, add = self.addition(l2.val + add)
                pointer = pointer.next
                l2 = l2.next
            pointer.next = l2

        return head.next

    def addition(self, temp):
        # judge carry-over
        if temp < 10:
            add = 0
        else:
            temp = temp % 10
            add = 1
        return ListNode(temp), add

    def extraction(self, l: ListNode):
        weight=1
        sum=0
        while l!=None:
            sum+=l.val*weight
            l=l.next
            weight*=10
        return sum

    def num2list(self,num:int):
        head=ListNode(0)
        pointer=head
        while num>0:
            pointer.next=ListNode(num%10)
            pointer=pointer.next
            num//=10
        return head.next
    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum=self.extraction(l1)+self.extraction(l2)
        if sum==0:
            return ListNode(0)
        else:
            return self.num2list(sum)

    # really elegant!! from @tusizi
    def addTwoNumbers3(self, l1, l2):
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next



if __name__ == '__main__':
    l1 = ListNode(1)
    # l1.next = ListNode(4)
    # l1.next.next = ListNode(3)
    # l1.next.next.next=ListNode(9)
    l2 = ListNode(9)
    l2.next = ListNode(9)
    # l2.next.next = ListNode(6)

    Solution().addTwoNumbers2(l1, l2)
