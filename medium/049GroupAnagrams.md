# 49. Group Anagrams
```
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

```

## Notes
检测一组字符串元素是否相同，即是求$f(str)=y$中的$f$，也就是需要设计一个**映射函数**。

暂时有如下三种想法：
1. 字符串排序。元素相同的字符串排序结果唯一；
2. 字符串中字母计数。将统计结果作为hash的对象；
3. 每个字母分配一个质数，遍历字符串，用字母对应质数相乘，将积作为hash对象。（from Leetcode discussion, quite brilliant) 

一点细节：Python3 字符不能直接相减，需要通过`ord()`转换为数值。