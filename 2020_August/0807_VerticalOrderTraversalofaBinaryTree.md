# Vertical Order Traversal of a Binary Tree



Given a binary tree, return the *vertical order* traversal of its nodes values.

For each node at position `(X, Y)`, its left and right children respectively will be at positions `(X-1, Y-1)` and `(X+1, Y-1)`.

Running a vertical line from `X = -infinity` to `X = +infinity`, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing `Y` coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of `X` coordinate. Every report will have a list of values of nodes.

 

**Example 1:**

![img](https://assets.leetcode.com/uploads/2019/01/31/1236_example_1.PNG)

```
Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation: 
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).
```

**Example 2:**

**![img](https://assets.leetcode.com/uploads/2019/01/31/tree2.png)**

```
Input: [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation: 
The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.
```

 

**Note:**

1. The tree will have between 1 and `1000` nodes.
2. Each node's value will be between `0` and `1000`.



# Solution

For nodes in same `x`, we have to maintain its **order** by **1. layer first,  2. small value comes first in the same layers**.

1. Layer-traversal. 

   ```python
   class Solution:
       def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
           if root is None:
               return []
           ans = [[] for _ in range(512)] # allocate all posititon
           base = 255 # since the tree will have between 1 and 1000 nodes. It's maximum wide should be 512
           qu = [[root,0+base]]
           
           # layer-traversal wit coordinate
           while len(qu)>0:
               record = {}
               for i in range(len(qu)):
                   
                   ans[qu[0][1]].append(qu[0][0].val)
                   if qu[0][1] not in record:
                       record[qu[0][1]] = 1
                   else:
                       record[qu[0][1]] += 1
                       
                   if qu[0][0].left is not None:
                       qu.append([qu[0][0].left,qu[0][1]-1])
                   if qu[0][0].right is not None:
                       qu.append([qu[0][0].right,qu[0][1]+1])
                       
                   qu.pop(0)
               # dealing nodes in same layer have same x
               for ele in record:
                   if record[ele]>1:
                       num = record[ele]
                       ans[ele][-num:] = sorted(ans[ele][-num:])
           
           # print([nodes for nodes in ans if nodes!= []])
           return [nodes for nodes in ans if nodes!= []]
   ```

2. pre-order traversal

   ```python
   class Solution:
       def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
           if root is None:
               return []
           self.ans = [[] for _ in range(512)] # allocate all posititon
           base = 255 # since the tree will have between 1 and 1000 nodes. It's maximum wide should be 512
           
           self.traversal(root,0+base,0)
           
           for nodes in self.ans:
               if nodes != []:
                   nodes.sort(key=lambda co:(co[1],co[0]))
           return [[node[0] for node in nodes] for nodes in self.ans if nodes !=[]]
           
       def traversal(self,root,x,y):
           if root is not None:
               self.ans[x].append([root.val,y])
               self.traversal(root.left,x-1,y+1)
               self.traversal(root.right,x+1,y+1)
   ```

   