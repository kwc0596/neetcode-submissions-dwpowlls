class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buy low and sell high. 
        #so we never buy and sell on the same day.
        #sell in the future so we cannot buy in the future and sell in the past.

        l, r = 0, 1 #l starts at first pos, r starts at pos after.

        maxP = 0

        while r < len(prices): 

            
            #we want to check when prices[r] > prices[l]
            #that way we can compare the profit gain. 
            if prices[r] > prices[l]: 
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)
                
            else: 
                l = r # set l to r since this is the new lowest price in the array
            r += 1
        return maxP

