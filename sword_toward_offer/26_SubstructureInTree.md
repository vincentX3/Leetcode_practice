# 26_SubstructureInTree

## 题目描述
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

## 思路
两步走。
1. 找树A节点值与树B根节点值相同的节点
2. 对该节点下子树检查

## Solution
```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        if pRoot1.val == pRoot2.val:
            result = self.test_subtree(pRoot1,pRoot2)
            if result:
                return True
        # search subtrees
        result_l = self.HasSubtree(pRoot1.left, pRoot2)
        result_r = self.HasSubtree(pRoot1.right, pRoot2)
        return result_l or result_r
    
    def test_subtree(self, ta,tb):
        # reach leave
        if not tb:
            return True
        
        if not ta or ta.val != tb.val:
            return False
        else:
            return self.test_subtree(ta.left,tb.left) and self.test_subtree(ta.right,tb.right)
```