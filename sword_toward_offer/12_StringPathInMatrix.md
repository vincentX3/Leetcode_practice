# 12_StringPathInMatrix

## 题目描述
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。 

## 思路
走迷宫求解，是一个解集树。无特别剪枝技巧，暴力回溯即可。代码细节多打磨下。

## Solution
``` python
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.s_matrix = None
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if len(path)==0:
            return False
        flag=False
        idx = 0
        self.s_matrix = [[0]*cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i*cols+j]==path[0]:
                    flag = self.search_path(matrix,rows, cols, i, j, path, idx)
                    if flag:
                        return True
        return False
    
    def search_path(self,matrix,rows, cols, i, j, path, idx):
        if idx == len(path):
            return True
        
        if i>=0 and j>=0 and i<rows and j<cols and self.s_matrix[i][j]!=1 and matrix[i*cols+j] == path[idx]:
            # match one char
            idx += 1
            self.s_matrix[i][j]=1
            found = self.search_path(matrix,rows, cols, i-1, j, path, idx) or self.search_path(matrix,rows, cols, i, j-1, path, idx) or  self.search_path(matrix,rows, cols, i+1, j, path, idx) or  self.search_path(matrix,rows, cols, i, j+1, path, idx)
            if found:
                return True
            else:
                self.s_matrix[i][j]=0
                return False
        else:
            return False
```