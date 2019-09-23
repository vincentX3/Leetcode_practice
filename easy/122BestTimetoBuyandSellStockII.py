from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0

        local_max=local_min=prices[0]
        trend=prices[1]-prices[0]
        profits=0
        for price in prices[1:]:
            if trend<=0:#previous price go down
                if price<=local_min:
                    local_min=price
                else:#turning point
                    trend=1
                    local_max=price
            else:#previous price go up
                if price>local_max:
                    local_max=price
                else:#turning point, the price goes down. sell precious stock!
                    profits+=local_max-local_min
                    trend=-1
                    local_min=local_max=price
        if trend>0:
            profits+=local_max-local_min
        return profits

    def maxProfit2(self, prices: List[int]) -> int:
        profits=0
        for i in range(len(prices)-1):
            if prices[i+1]-prices[i]>0:
                profits+=prices[i+1]-prices[i]
        return profits