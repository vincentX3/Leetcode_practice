# 33_SquenceOfBST

## 题目描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

## 思路
对于后序遍历的二叉**搜索树**，可分为三个部分：
$$[left sub-tree squence, rigt sub-tree, root node]&&，
其中左子树序列值都小于根节点值，右子树序列值都大于根节点值。

若不满足上述划分则非二叉搜索树的BST。
故**递归**处理每个节点即可。
注意空结点的处理。

## Solution
```python
# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False
        elif len(sequence) == 1:
            return True
        elif len(sequence) == 2:
            return True if sequence[0] < sequence[1] else False 
        # len >= 3
        idx_split = -1
        flag = False
        for idx, val in enumerate(sequence[:-1]):
            if val > sequence[-1]:
                idx_split = idx
                flag = True # found split index
            if flag:
                # check order
                if  val < sequence[-1]:
                    return False
        # check sub-sequence
        left = True if idx_split == 0 else self.VerifySquenceOfBST(sequence[:idx_split])
        right = True if idx_split == -1 else self.VerifySquenceOfBST(sequence[idx_split:-1])
        return left and right
```