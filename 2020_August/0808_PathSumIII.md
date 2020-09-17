# Path Sum III



You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

**Example:**

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



# Solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root==None:
            return 0
        here = self.trace(root, sum) #对于每个节点，视其为树根
        left = self.pathSum(root.left, sum) 
        right = self.pathSum(root.right, sum)

```python
    return here + left + right

def trace(self, root, sum):
    # 求解树根节点到各个节点的路径和等于sum的个数
    if root == None:
        return 0
    else:
        left = self.trace(root.left, sum - root.val)
        right = self.trace(root.right, sum - root.val)
        here = 1 if root.val == sum else 0
        return left + right + here
```
