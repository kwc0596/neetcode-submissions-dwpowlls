class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #you may decide your bananas per hour eating rate of k. Each hour, you may choose a pile of bananas and eats
        #k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not
        #eat from another pile in the same hour. 

        #binary search to look within the range of 1 to largest set of bananas in the pile. that will be our largest number
        #per hour to eat.

        #can set max res before doing binary search as the max

        

        l, r = 1, max(piles)
        res = r
        #how to proceed here.. 

        #we will iterate through piles to determine the amount of hours it takes to eat the bananas. 

        #while loop to use binary search algorithm. 
        while l <= r: 
            #midpoint that we usually set to m. we will set to k because k is the eating rate. we're looking through the possible
            #time to have the slowest rate where we can eat within a certain time frame based off of h. 
            k = (l + r) // 2
            hours = 0 #set our hours equal to 0 for each loop because we are checking the rate of k how many hours
            #it will take.
            #for loop to calculate hours total taken to eat the bananas. 
            for p in piles: 
                hours += math.ceil(p / k)
            #compare time taken to our current res which is the max time it will take. If it is smaller, we can
            #compare res to hours and update new minimum. 
            #also decrement k by 1 to continue binary search. 
            if hours <= h: 
                res = min(res, k) #comparison is between res and k. hours is the total time taken to eat bananas. k is the rate. as is res.
                r = k - 1
            else: 
                #check if hours is greater than res. if it is, then you know we need to find larger values since the rate was
                #too small. its too small because the hours taken is greater than our current res. 
                l = k + 1
        return res

