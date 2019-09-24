# 125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

> Input: "A man, a plan, a canal: Panama"  
Output: true  
>

Example 2:

> Input: "race a car"  
Output: false
>

---
## Solution:
简单的回文判断。
1. Python字符串处理
python提供对str处理的包和函数尚算不错。  
直接：**1. 去空格、标点 2. 统一大小写 3. 逆序字符串并比较** 即可

2. 头尾双指针遍历
不复杂，就没写了。