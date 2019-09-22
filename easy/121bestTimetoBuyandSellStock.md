# 121. Best Time to Buy and Sell Stock

Say you have an array for which the $$ith$$ element is the price of a given stock on day $$i$$.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

> Input: [7,1,5,3,6,4]  
Output: 5  
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:

> Input: [7,6,4,3,1]  
Output: 0  
Explanation: In this case, no transaction is done, i.e. max profit = 0.

---
## Solutions
1. Time Limit Exceeded: 暴力求差值
最为直接的方法，莫过于每日价格间**两两求差值**，差值越小（负数），则利润越高。差值最小值都大于零，则无利润可赚。  
但显然，此方法是**O(N^2**复杂度的，提交后果然超时。

2. 分析股值走势的特征
此题刚接触时，最为恼人的是不知如何决断：**何时取得最大差值**。细思量后恍然大悟：  
最大利润是**局部**最低价与**局部**最高价的差值——废话。
在时间序列中，利润的更新只与**全局最低价**的刷新及更高售价的刷新有关，即，不用顾虑此前的局部低价和当前高价间的差价，能大于全局最低价和当前高价间的差价。