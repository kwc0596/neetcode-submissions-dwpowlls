class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #so our lower bound would be the max weight one package. and the upper bound would be the sum of all packages.

        l, r = max(weights) , sum(weights) 

        res = r

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
                r  = cap - 1
            else: 
                l = cap + 1
        return res
