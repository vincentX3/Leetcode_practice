# 34_PathInTree

## 题目描述
输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)

## 思路
求全部解，即求**解集树**，典型的**回溯法**求解。  
使用全局变量方便传参，每个节点处理后要更新`path`。
> `python`一切皆为对象，list做参数传递时是**浅复制**，小心坑。

## Solution
```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.ans = []
        self.path = []
         
    def find_paths(self, root, n):
        # n = expectNumber - current_sum
        path = self.path
        n -= root.val
        path.append(root.val)
        if root.left == root.right == None:
            if 0 == n: self.ans.append(path[:])
        if root.left: self.find_paths(root.left, n)
        if root.right: self.find_paths(root.right, n)
        path.pop()
        
    def FindPath(self, root, expectNumber):
        # write code here
        if not root: return []
        self.find_paths(root, expectNumber)
        self.ans.sort(key=lambda x:len(x),reverse=True)
        return self.ans
```