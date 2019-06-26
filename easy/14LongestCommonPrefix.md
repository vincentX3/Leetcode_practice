# 14. Longest Common Prefix


Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

Example 1:

> Input: ["flower","flow","flight"] 
Output: "fl"

Example 2:

> Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters `a-z`


---
### Solution
1. 利用切片功能，在两两比较过程中不断更新`prefix`  
    1. 判断`strs`，空则直接返回`""`
    2. 预取`prefix`等于第一个`str`
    3. 取下一个字符串
    3. 长度调整。比较`prefix`和下一个字符串的长度。若`prefix`更长，则切片至和下一字符串等长
    4. 使用下标逐一比较`prefix`和字符串，直至下标处字符不相等。更新`prefix=prefix[:i]`
    6. 若仍有字符串，执行`3.`
2. 他人的`solution`，非常优雅且**pythonic**。活用了`min.max()`,`enumerate()`  
分析：一组字符串中，
    - 共同前缀必然是最**短**字符串的**子集**。
    - 若有共同前缀，则最**长**、**码表值最大**的字符串必然也包含它。
    - 满足上述，则其余都包含该前缀

    `min()`/`max()`对字符串序列操作，返回的是码表值最大/小的字符串。意味着该字符串长度最长/短，且等长字符串中码值亦最小。
    用`enumerate()`来遍历、比较就比用`for i in range(len(str))`来得优雅太多了