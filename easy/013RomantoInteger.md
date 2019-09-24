# 13. Roman to Integer

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.


> Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

> Input: "III"
Output: 3

Example 2:

> Input: "IV"
Output: 4

Example 3:

> Input: "IX"
Output: 9

Example 4:

> Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:

> Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

---
### solution
1. 自己很直接的想法。将特殊情况如`IX`也加入`dict`。读字符串时先`get`两位的字符，如果不在`dict`内，则取当前字符对应值。
2. 罗马数字转换无非关系到**顺序与加减**而已。设有字符串`AB`，若`dict[A]`小于`dict[B]`，则说明为减法情况，直接减去`dict[A]`；否则就加`dict[A]`
3. Discuss中看到的，**暴力**又高效。直接用`str.replace`替换特殊情况为对应一般数值
    > e.g. 'IX' -> 'XIIII'