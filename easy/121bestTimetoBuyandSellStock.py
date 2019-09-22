from typing import List


class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        # Time Limit Exceeded
        if len(prices)<2:
            return 0
        profits = []
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profits.append(-(prices[i] - prices[j]))
        profits.sort()
        profit = profits[-1]
        if profit < 0:
            return 0
        else:
            return profit

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        minimum=prices[0]
        profit=0
        for price in prices[1:]:
            if price<minimum:
                minimum=price
            elif profit<price-minimum:
                profit=price-minimum
        return profit