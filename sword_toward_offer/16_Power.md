# 16_Power16_Power

## 题目描述
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

保证base和exponent不同时为0

## 思路
很多细节处理：
1. 负指数判断处理
2. 底数为0时的异常处理（边界值处理）
3. 如何高效计算？

## Solution
```python
# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0:
            return 0
        negative = False
        if exponent < 0:
            negative = True
        exponent = abs(exponent)
        result = self.pos_power(base,exponent)
        if negative:
            result = 1/result
        return result
    
    def pos_power(self, base, exponent):
        if exponent == 0:
            return 1
        half = self.pos_power(base,exponent//2)
        if exponent & 1:
            return base*half*half
        else:
            return half*half
```