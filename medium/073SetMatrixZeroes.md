73. Set Matrix Zeroes

```
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
```

## Notes
> 想了蛮久还是看别人的思路了，蛮有趣的题。

要求O(1)空间，做到in-place，但我们发现，当遇到一个元素为0的时候，我们需要记住其行号、列号。  
那么思考，我们怎样善用矩阵本身作为容器呢？  
不妨吧第一行、第一列作为容器，当`[i][j]==0`时置`matrix[0][j], matrix[i][0] = 0, 0`作为标记，把mxn矩阵退化为(m-1)x(n-1)的矩阵。

接下来再次遍历矩阵，若该单元的第一行或第一列的元素值为0，则置该单元为0。  
同时，第一行、第一列是否要清零呢？ 这就要在第一次遍历时做好标记。