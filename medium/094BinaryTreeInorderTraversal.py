from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal_recursive(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        traversal, stack = [], [[root, 1]]
        cur = [root.left, 0]
        while len(stack) > 0 or cur[0]:
            print(stack,cur,traversal)
            if not cur[0]:
                cur = stack.pop()
            elif cur[0].left and cur[1] == 0:
                cur[1] = 1
                stack.append(cur)
                cur = [cur[0].left, 0]
            else:
                traversal.append(cur[0].val)
                cur = [cur[0].right, 0]

        return traversal

    def inorderTraversal_clear(self, root):
        ans = []
        stack = []

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmpNode = stack.pop()
                ans.append(tmpNode.val)
                root = tmpNode.right

        return ans


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(s.inorderTraversal(root))
