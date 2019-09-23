# 122. Best Time to Buy and Sell Stock II

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

> Input: [7,1,5,3,6,4]  
Output: 7  
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Example 2:

> Input: [1,2,3,4,5]  
Output: 4  
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.


Example 3:

> Input: [7,6,4,3,1]  
Output: 0  
Explanation: In this case, no transaction is done, i.e. max profit = 0.

---
# Solutions:
> 似乎我总有能化简为繁的能力。
1. 标记**转折点**  
画折线图可知，利润为局部最小值与局部最大值的差值。每个折线的“谷底”即为局部最小值，“尖峰”为局部最大值，当遇到局部最大值后即可对本段利润进行“收获”。  
切记，最后一天不一定能遇到“尖峰”的转折，要单独检测处理。
2. 遍历累加啊蠢！
其实没上述那么复杂。上述思路基于对股票买卖的**模拟**——买进卖出，但事实上我们的总利润，就是每段上涨**折线段**的加和。  
所以，只需要遍历，两两判断，有涨就加即可。