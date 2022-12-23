class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def rec(i , isBuy):
            if i >= len(prices): return 0
            
            if (i , isBuy) in memo:
                return memo[(i , isBuy)]
            
            cooldown = rec(i+1 , isBuy)
            
            if isBuy:
                buy = rec(i+1 , not isBuy) - prices[i]
                memo[(i , isBuy)] = max(cooldown , buy)
            else:
                sell = rec(i+2 , not isBuy) + prices[i]
                memo[(i , isBuy)] = max(cooldown , sell)
            return memo[(i , isBuy)]
        return rec(0 , True)
