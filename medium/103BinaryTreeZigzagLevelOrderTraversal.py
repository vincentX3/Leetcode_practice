# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res=[]
        l_stack,r_stack=[root],[]
        direction='left'
        while (direction=='left' and len(l_stack)>0) or (direction=='right' and len(r_stack)>0):
            temp=[]
            if direction=='left':
                while len(l_stack)>0:
                    node = l_stack.pop()
                    temp.append(node.val)
                    if node.left:
                        r_stack.append(node.left)
                    if node.right:
                        r_stack.append(node.right)
            else:
                while len(r_stack)>0:
                    node = r_stack.pop()
                    temp.append(node.val)
                    if node.right:
                        l_stack.append(node.right)
                    if node.left:
                        l_stack.append(node.left)
            direction = 'right' if direction=='left' else 'left'
            res.append(temp)
            
        return res
        