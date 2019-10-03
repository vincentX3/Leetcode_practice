# 342. Power of Four

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

> Input: 16  
Output: true

Example 2:

> Input: 5  
Output: false

Follow up: Could you solve it without loops/recursion?
---
## Solutions:
看着很简单的题，没想到还有如此趣味的解法，**数学真奇妙**。
1. 循环移位
判断是否4的幂和判断是否2的幂同理，不断求模判断余数、除4即可。略tricky些就以移位代替除法，性能略略提升。
2. 转为字符串统计
数为4的幂的二进制表示，如`16=0b1000`、`64=0b1000000`。特点是有且仅有1个1（最高位的1），并且有偶数个0。  
转为二进制表示的串计数判断即可。
3. 数论：4的幂的特征分析
    > reference：[**@lucifer**](https://github.com/azl397985856) 
    1. 是4的幂，则是2的倍数，且减一为3的倍数
    ```python
       return num%2==0 and (num-1)%3==0
    ```
    2. 32bit signed integer，二进制表示下有且仅有1个**1**，且在**奇数**位置上。如何判别实现？👇👇
    ```python
       return num & 0x55555555 == num 
       # 0x55555555=0b 01010101010101010101010101010101 (32-bit)
    ```