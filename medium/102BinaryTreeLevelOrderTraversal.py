# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res = []
        qu = [root]
        num = 1
        while num > 0:
            cur_level = []
            for _ in range(num):
                temp = qu.pop(0)
                cur_level.append(temp.val)
                if temp.left:
                    qu.append(temp.left)
                if temp.right:
                    qu.append(temp.right)
            res.append(cur_level)
            num = len(qu)

        return res

    # elegant list compression
    def levelOrder_leetcode(self, root):
        # @ cmc
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            LRpair = [(node.left, node.right) for node in level]
            level = [leaf for LR in LRpair for leaf in LR if leaf]
        return ans