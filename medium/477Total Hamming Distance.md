# 477. Total Hamming Distance

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.

Example:
```
Input: 4, 14, 2

Output: 6

Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
```

Note:
Elements of the given array are in the range of 0 to 10^9
Length of the array will not exceed 10^4.

---
## solution
1. **Exceeded Time Limitied
*hamming distance* 可谓是CS undergraduate的老朋友了，大家不一定真的懂，但总归混了个脸熟。  
都知道两数间的*hamming distance*是两数**二进制取异或XOR后结果中1的个数**，于是很直观的思路，便是：  
    > 双重循环遍历list元素，两两配对。  
结对后使用`^`求异或并python built-in 函数`bin()`将结果转为二进制串，统计其中“1”的个数。

几行写完，欢天喜地的submit，发现超时了。冷静一想，$$O(n^2)$$的时间复杂度确实不好看。

2. 移位统计
不才，看了眼讨论区才恍然大悟——$$O(n)$$的实现只需统计每个位上1的个数！  
原理是直接的，设$$k_i$$为`nums`中第i位（二进制下）上1的总个数，$$len(nums)==n$$,显然$$n-k_i$$为第i位上0的个数。  
考虑**异或**，每个1与$$n-k_i$$个0求异或，加和即为$$n-k_i$$，故每位上的hamming distance即为$$k_i*(n-k_i)$$。  
综上，总的hamming distance即为各个位上距离的和。

> 代码中有个小trick，用1做掩码来做与运算。