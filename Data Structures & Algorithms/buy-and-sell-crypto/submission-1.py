class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        #we want to buy low and sell high. 

        #in a two pointer approach, l would be low and r would be high. 

        l, r = 0, 1

        maxP = 0

        while r < len(prices): 
            
            if prices[r] > prices[l]:

                profit = prices[r] - prices[l] 

                maxP = max(profit, maxP)
            
            else: 
                l = r #we don't increment 1 . we move the value to r because r had the new lowest min.
            r += 1

        return maxP

