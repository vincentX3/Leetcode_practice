# 14_CuttingRope

## 题目描述
给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1），每段绳子的长度记为k[0],k[1],...,k[m]。请问k[0]xk[1]x...xk[m]可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

## 思路
这似乎是数学问题？ 姑且算作**贪心**吧。
简单说，有$3$选$3$，没$3$选$2$.
注意要求是：**至少剪一刀**，处理好`number ==2 or number == 3`的情况。

## Solution
```python
# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        # write code here
        if number==2:
            return 1
        if number==3:
            return 2
        if number%3==1:
            return 3**(number//3-1)*4
        elif number%3==2:
            return 3**(number//3)*2
        else:
            return 3**(number//3)
```