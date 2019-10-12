#5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
```
Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"  
Output: "bb"
```
---
## Solutions:
实话实说，这题对目前榆木脑阔的我而言，费神许久也没得解。便是好好欣赏、学习已有的算法吧！
1. 只能处理约length<20的递归解  
自己尝试解题的思路。算法中使用dict来存已经检测过的字符串。算是对Easy阶段学习的分治法与活用hash的应用。当然，这个算法仍旧很慢TAT
2. 动态规划  
分析回文字符串的构成，发现有如下定义：  
$$
P(i, j)=\left\{\begin{array}{ll}{\text { true, }} & {\text { if the substring } S_{i} \ldots S_{j} \text { is a palindrome }} \\ {\text { false, }} & {\text { otherwise. }}\end{array}\right.
$$  
对于子串为回文的串，若左右各添上相同字符，则仍旧是回文串，即：  
$$
P(i, j)=\left(P(i+1, j-1) \text { and } S_{i}==S_{j}\right)
$$  
对于起始状态，有两种可能，单字符如'a'，为回文，双相同字符如'aa'，为回文，即：  
$$
\begin{array}{l}{P(i, i)=\text { true }} \\ {P(i, i+1)=\left(S_{i}==S_{i+1}\right)}\end{array}
$$  
据此迭代，我们可建立二维数组存储每个状态信息，进行回文串检测。
3. 动态规划levelup——O(1) space  
上述已讨论了回文串的的核心：
    > 对于子串为回文的串，若左右各添上相同字符，则仍旧是回文串  
                                               
    因而，我们可以通过下标遍历整个字符串，以每个字符串下标为基准，**向左右扩张**检测回文串，即有：
    ```python
    def expand_check(self,s,left,right):
        while s[left]==s[right]:
            left-=1
            right+=1
            if left<0 or right>=len(s):
                break
        return s[left+1:right]
    ```
   实现时要记得，基础回文串有两种：'a' 和 'aa'
 4. Manacher's algorith  
 wiki: https://en.wikipedia.org/wiki/Longest_palindromic_substring
 待深入研究
