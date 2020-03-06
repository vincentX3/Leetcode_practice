# 05_ReplaceSpaces

## 题目描述
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

## 思路
考察**变长字符串的处理**。
若是原字符串替换。从前向后遍历替换，$O(n^2)$复杂度；  
双指针，从后往前挪，$O(n)$

## Solution

python字符串可变长，比较灵活。
``` python
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        
        #pythonic
        #v1
        return '%20'.join(s.split(' '))

        #v2
        return s.replace(' ','%20')

        #v3
        ptr = 0
        for i in range(len(s)):
            if s[ptr]==' ':
                s=s[:ptr]+'%20'+s[ptr+1:]
                ptr+=3
            else:
                ptr+=1
        
        return s
            
# t1='We are happy'
# t2=''
# t3='  '
```