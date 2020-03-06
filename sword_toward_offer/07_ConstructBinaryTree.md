# 07_ConstructBinaryTree

## 题目描述
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

## 思路
先序序列的第一位必然是root，在中序序列中找到root.index后，[:root.index]为左子树结点，[root.index+1:]为右子树结点。
缩减问题规模，递归求解即可。
> 子树val不能重复，否则中序序列无法定位。

## Solution
``` python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None
        node = TreeNode(pre[0])
        for i,val in enumerate(tin):
            if val==pre[0]:
                mid = i
                break
                
        node.left = self.reConstructBinaryTree(pre[1:mid+1],tin[:mid])
        node.right = self.reConstructBinaryTree(pre[mid+1:],tin[mid+1:])
        
        return node
```
