class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #lower and upper bound 
        l, r = max(weights) , sum(weights) 

        res = r

        #helper function to check if capacity exceeds more than a day

        def canShip(cap): 

            ship, currCap = 1, cap

            for w in weights: 

                #for loop to iterate through weights array

                if currCap - w < 0: 
                    #condition to check if currCap is too small
                    ship += 1
                    currCap = cap 
                
                currCap -= w

            return ship <= days
        
        while l <= r:
            cap = (l + r) // 2

            if canShip(cap): 
                res = min(res, cap)
                r = cap - 1
            else: 
                l = cap + 1
        return res