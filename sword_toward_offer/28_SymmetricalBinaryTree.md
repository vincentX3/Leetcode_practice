# 28_SymmetricalBinaryTree

## 题目描述
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。

## 思路
- 对称的树，一定是**完全树**。
- 对称的树，每层节点值左右对称。
so，
**层序遍历**，每遍历一层，检查该层的值是否左右对称。
> 细节：对于`None` 空结点要用占位符处理。

## Solution
```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        level = 1
        qu = [pRoot]
        while qu:
            # level order traversal
            val_seq = []
            for _ in range(level):
                if len(qu)>0:
                    node = qu.pop(0)
                    if node:
                        val_seq.append(node.val)
                        # add next level nodes
                        qu.append(node.left if node.left else None)
                        qu.append(node.right if node.right else None)
                    else:
                        val_seq.append('#') # Null node
                        qu.append(None)
                        qu.append(None)
                else:
                    return False
            if not self.is_mirror(val_seq):
                return False
            elif self.is_leaf(qu):
                return True
            else:
                level *=2
        return False
    
    def is_mirror(self,seq):
        length = len(seq)
        for i in range(length//2):
            if seq[i]!=seq[length-i-1]:
                return False
        return True
    
    def is_leaf(self,qu):
        for node in qu:
            if node:
                return False
        return True
```                