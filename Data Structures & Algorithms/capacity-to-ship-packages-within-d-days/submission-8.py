class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #we don't know what the maximum weight is. 
        # we want to find what the least weight capacity is. 
        #i know we need a helper function but i don't particularly know why. 

        #the helper function is there to iterate through a loop of each weight to determine if the capacity we're at
        #can hold the weights within a certain amount of days. I think the benefit is to save us from code writing. 
        def canShip(cap): 
            ships, currCap = 1, cap

            for w in weights: 
                if currCap - w < 0: 
                    ships += 1
                    currCap = cap
                currCap -= w
            return ships <= days
        
        l, r = max(weights), sum(weights)
        res = r


        while l <= r: 
            cap = (l + r) // 2

            if canShip(cap):
                res = min(cap, res) 
                r = cap - 1
            else: 
                l = cap + 1
        return res

