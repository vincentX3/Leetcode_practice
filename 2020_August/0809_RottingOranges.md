# Rotting Oranges

Solution

In a given grid, each cell can have one of three values:

- the value `0` representing an empty cell;
- the value `1` representing a fresh orange;
- the value `2` representing a rotten orange.

Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return `-1` instead.

 

**Example 1:**

**![img](https://assets.leetcode.com/uploads/2019/02/16/oranges.png)**

```
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
```

**Example 2:**

```
Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
```

**Example 3:**

```
Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
```

 

**Note:**

1. `1 <= grid.length <= 10`
2. `1 <= grid[0].length <= 10`
3. `grid[i][j]` is only `0`, `1`, or `2`.

# Solution

1. Brutal simulation

   ```python
   import copy
   
   class Solution:
       def orangesRotting(self, grid: List[List[int]]) -> int:
           
           # helper
           def update(x,y):
               # rot orange
               # return False when nothing change
               change = False
               if x > 0 and grid[x-1][y] == 1:
                   change = True
                   next_grid[x-1][y] = 2
               if x < high-1 and grid[x+1][y] == 1:
                   change = True
                   next_grid[x+1][y] = 2
               if y > 0 and grid[x][y-1] == 1:
                   change = True
                   next_grid[x][y-1] = 2
               if y < wide-1 and grid[x][y+1] == 1:
                   change = True
                   next_grid[x][y+1] = 2
               return change
               
           
           # brutal
           has_fresh, change = True, False
           count, high, wide = 0, len(grid), len(grid[0])
           while has_fresh:
               # traversal the grid
               has_fresh, change = False, False
               next_grid = copy.deepcopy(grid)
               for i in range(high):
                   for j in range(wide):
                       if grid[i][j] == 1:
                           has_fresh = True
                       elif grid[i][j] == 2:
                           if update(i,j):
                               change = True
               if not has_fresh or not change:
                   break
               else:
                   count += 1
                   grid = next_grid
                   # print(grid)
           if not change and has_fresh:
               count = -1
           return count	
   ```

2. BFS for simulation.

   ```python
   class Solution:
       def orangesRotting(self, grid: List[List[int]]) -> int:
           q=[]
           count=0
           for i in range(len(grid)):
               for j in range(len(grid[0])):
                   if grid[i][j]==2:
                       q.append((i,j,0))
                   if grid[i][j]==1:
                       count+=1
           step=0
           while q:
               i,j,step=q.pop(0)
               for r,c in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                   if 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c]==1:
                       grid[r][c]=2
                       count-=1
                       q.append((r,c,step+1))
           if count>0:
               return -1
           else:
               return step
   ```

   