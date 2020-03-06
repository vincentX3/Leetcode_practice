# 04_FindInPartiallySortedMatrix

## 题目描述:
> 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

## 思路：
- 二维数组要正确理解，切莫简化为如[1-9]递增的模式。若为逐行逐列递增，则退化为一维递增数组。
- 以此数组为例：
```
0  3  8
1  5  9
4  6  10
```
要在数组上移动，取左上角或右下角极值点，则当`val != target`时，`next val`有两个移动方向；
又发现右上角或左下角为起点时，每次比较可只关注行或列的移动。

## Solution
``` python

class Solution:
    # array 二维列表
    def Find(self, target, array):
        if not array:
            return False
        # check boundary
        if target < array[0][0] or target > array[-1][-1]:
            return False
        # search by grids
        row, col = 0, len(array[0])-1
        while col>=0 and row< len(array): # boundary
            if array[row][col] > target:
                col-=1
            elif array[row][col] < target:
                row+=1
            else:
                return True
        
        return False

```