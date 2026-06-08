class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights) #lower and upper bounds to find least weight capacity. 
        #these are the bounds because if we set the lower bound the be lower than the max, then the highest weight 
        #in weights would never be able to packaged and shipped. The sum of weights is the upper bound because, this 
        #is the capacity we know it is also capable of, just really high, because it encapsulates every single weight
        #on the conveyor belt. But we are looking for the least weight capacity. 
        #since this is a least value type problem, we want to have a result that stores the lowest at the time
        #and does a comparison in the while loop that compares minimum values. 

        res = r #this is the lowest at the time we know will work based off of days. max weight could work but not necessarily
        #because this value could be impacted by the days given. 

        
        #we need to use a helper function to check and see if the number is able to match or be less than the number of days
        #taken to hold packages. 

        def canShip(cap): 
            ships, currCap = 1, cap
            for w in weights: 
                if currCap - w < 0: 
                    ships += 1
                    currCap = cap
                currCap -= w
            return ships <= days
        
        while l <= r: 
            cap = (l + r) // 2
            if canShip(cap): 
                res = min(cap, res)
                r = cap - 1
            else: 
                l = cap + 1
        return res