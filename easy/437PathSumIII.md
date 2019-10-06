# 437. Path Sum III

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:
```
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
```

---
## Solutions:
1. 暴力递归
题目看着头大：二叉树任意节点和其后代节点的值的和等于目标。但我们要把握问题的核心：  
    > 从根节点起，至各个后代节点的路径和，有否等于目标值。  
                                                       
    对于**任意节点**其实**等价于每个节点视作根节点**，对其子树进行遍历。
    至此，可得递归算法。
    
2. hash
    > reference：thanks for [this brilliant explanation](https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-%3A-) by *wonderlives*
    
    暴力递归时的缺陷，在于对于每一个节点都重新计算其子树的全部路径和，导致了大量**重复运算**。
    使用**hashmap**来保存中间的路径和，空间换时间。
    
    temporary：详见reference
    // TODO：思路解析