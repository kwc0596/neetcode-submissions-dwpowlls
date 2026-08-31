class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buy low, sell high. 

        #l pointer will start at first pos. r pointer will start at following pos. 

        l, r = 0, 1

        #set up max profit variable 
        maxP = 0

        while r < len(prices): 
            
            if prices[r] > prices[l]: 
                
                profit = prices[r] - prices[l]

                maxP = max(maxP, profit)
                #no need to increment l
                r += 1
            
            else: 
                l = r
                r += 1
        return maxP

