# 30_MinInStack

## 题目描述
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
注意：保证测试中不会当栈为空的时候，对栈调用pop()或者min()或者top()方法。

## 思路
分析时，发现哪怕把最小值留在栈顶，当出栈后求下一最小值，仍需要排序；
故空间换时间，引入同步的最小值栈。

## Solution
```python
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.s = []
        self.s_min = []
        
    def push(self, node):
        # write code here
        self.s.append(node)
        if len(self.s_min) == 0:
            self.s_min.append(node)
        elif node < self.s_min[-1]:
            self.s_min.append(node)
        else:
            self.s_min.append(self.s_min[-1])
            
    def pop(self):
        # write code here
        self.s_min.pop()
        return self.s.pop()
    
    def top(self):
        # write code here
        return self.s[-1]
    
    def min(self):
        # write code here
        return self.s_min[-1]
```