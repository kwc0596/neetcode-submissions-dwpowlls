class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Sliding window 

        #can't sort

        #find the min value? 

        #immediately set min value at prices[0]

        #check if neighbor value is smaller.

        #if it is neighbor value because new min. 

        #we continue checking this until neighbor value is higher. 

        #first time this is true that is our profit.

        #we continue searching r pointer until profit can be higher.

        l, r = 0, 1 #l Buy, r Sell

        maxP = 0 

        while r < len(prices): 
            
            #find maxP 

            if prices[l] < prices[r]: #checks to see if l value is less than r value
                profit = prices[r] - prices[l] #finds profit for difference

                maxP = max(profit, maxP) #compares to max profit value
            else: 
                l = r #if l value is equal or greater than r, we will move l value. 
                
            r += 1
        return maxP



