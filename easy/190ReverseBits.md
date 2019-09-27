# 190. Reverse Bits

Reverse bits of a given 32 bits unsigned integer.

 

Example 1:

> Input: 00000010100101000001111010011100  
Output: 00111001011110000010100101000000  
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

Example 2:

> Input: 11111111111111111111111111111101  
Output: 10111111111111111111111111111111  
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10101111110010110010011101101001.
 

Note:

> Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above the input represents the signed integer -3 and the output represents the signed integer -1073741825.
 

Follow up:

If this function is called many times, how would you optimize it?

---
## Solutions
1. 转换为str进行翻转
    将int转为字符串，反转后再转回int。注意，字符串记得补齐为32位长度
    实现：
    1. **pythonic**，基于python`list`提供的优雅的**slice**
    2. **divide and conquer**。  
        大问题：翻转字符串，子问题：二分后翻转子串。  
        出口条件：字符串长度为一，无须反转。
        归并：两翻转的子串前后交换
2. 位运算
    循环，将输入的数末位移出，加到`result`中，`result`每轮左移1位（即实现*2）