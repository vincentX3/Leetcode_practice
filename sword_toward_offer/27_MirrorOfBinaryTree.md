# 27_MirrorOfBinaryTree

## 题目描述
操作给定的二叉树，将其变换为源二叉树的镜像。

## 思路
考虑每个子树交换子节点。递归

## Solution
```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        # reach bottom
        if not root:
            return root
        # have children
        mirror_l = self.Mirror(root.left)
        mirror_r = self.Mirror(root.right)
        root.left, root.right = mirror_r, mirror_l
        return root
```