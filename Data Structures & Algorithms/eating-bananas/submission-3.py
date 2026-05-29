class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #we want to return the minimum integer k such that you can eat all the bananas within h hours. 

        l, r = 1, max(piles)
        res = r

        hours = 0
        while l <= r:  
            k = (l + r) // 2
            hours = 0
            for p in piles: 

                hours += math.ceil(p / k) #round up for any decimal value. (p / k) is our eating rate. 

            if hours <= h: 
                res = min(res, k)

                r = k - 1
            else: 
                l = k + 1
        return res

