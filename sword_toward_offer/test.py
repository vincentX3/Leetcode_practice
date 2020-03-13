# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return None
        else:
            paths = self.find_paths(root, expectNumber, 0, [])
            paths.sort(key=lambda x:len(x)) #sorted by length
            return paths
    
    def find_paths(self, root, expectNumber, cur_sum, cur_path):
        print(root.val,cur_path)
        if not root.left and not root.right: # is leave
            if cur_sum + root.val == expectNumber:
                cur_path.append(root.val)
                print(root.val,[cur_path])
                return [cur_path]
            else: return []
        else:
            cur_path.append(root.val)
            cur_sum += root.val
            left_paths = self.find_paths(root.left, expectNumber, cur_sum, cur_path.copy()) if root.left else []
            right_paths = self.find_paths(root.right, expectNumber, cur_sum, cur_path.copy()) if root.right else []
            print(root.val,left_paths,right_paths)
            return [*left_paths, *right_paths]
                

if __name__ == '__main__':
    s = Solution()
    # my_list = ListNode(0)
    # my_list.next = ListNode(1)
    # my_list.next.next = ListNode(2)
    # my_list.next.next.next = my_list.next
    t =TreeNode(8)
    t.left = TreeNode(3)
    t.right = TreeNode(16)
    t.left.left = TreeNode(13)
    foo = s.FindPath(t,24)
    print('result:',foo)
