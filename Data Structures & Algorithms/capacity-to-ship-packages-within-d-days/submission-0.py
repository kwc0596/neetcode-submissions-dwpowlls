class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # do you then determine what the maximum is based off of the highest weight
        #in the array? if so, then you can come with some type of algorithm to find
        #if that weight can be shipped off in the given amount of days. 

        #however, you also have to ship the packages in order. 

        #so the first thing to do would be to sort the array. 


        #i think finding the sum of the array and dividing by days doesn't automatically
        #give you a response because it has to be shipped in order. 

        l, r = max(weights), sum(weights)
        res = r #since this is the max upper bound we can possibly use. 

        def canShip(cap) : 
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
                res = min(res, cap)
                r = cap - 1
            else: 
                l = cap + 1
        return res

        