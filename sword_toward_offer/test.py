# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
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
            print(ptr.val)
            while ptr.next and ptr.next.val == cur_val:
                print(ptr.next.val)
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

if __name__ == '__main__':
    s = Solution()
    my_list = ListNode(0)
    my_list.next = ListNode(1)
    my_list.next.next = ListNode(1)
    
    foo = s.deleteDuplication(my_list)
    print('result')
    while foo:
        print(foo.val)
        foo = foo.next
