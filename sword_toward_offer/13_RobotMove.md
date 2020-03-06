# 13_RobotMove

## 题目描述
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？

## 思路
最初的想法是找到一个数学规律，但深究题意后发现能到达的地方还是由移动直接联系的，那就继续当迷宫来走吧。  
简单画图可知，对于$m*n$的矩阵方格，越往右下下角，数位和越大，越难走到。很直观的想到，使用**BFS**搜索。

## Solution
``` python
# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        if threshold < 0:
            return 0
        visited = [ 0 for _ in range(rows*cols)]
        qu, grid = [[0,0]], None
        count = 0
        while qu!=[]:
            grid = qu.pop()
            if self.get_sum(grid) <= threshold and visited[grid[0]*cols+grid[1]]!=1:
                print(grid)
                visited[grid[0]*cols+grid[1]] = 1
                count +=1
                if grid[0]-1 >0:
                    qu.append([grid[0]-1,grid[1]])
                if grid[1]-1 >0:
                    qu.append([grid[0],grid[1]-1])
                if grid[0]+1 <rows:
                    qu.append([grid[0]+1,grid[1]])
                if grid[1]+1 <cols:
                    qu.append([grid[0],grid[1]+1])  
            
        return count
    
    def get_sum(self, grid):
        sum_grid = 0
        for num in grid:
            while num > 0:
                sum_grid += num%10
                num //=10
        return sum_grid
```