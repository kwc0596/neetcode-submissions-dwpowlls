import math
class Solution:
    def mySqrt(self, x: int) -> int:
        #what the hell does this have to do with binary search? 
        #we cannot use built in exponent functions or operators? 

        # my first guess is to create an array that lists all the values from 1 to x. 

        #calculate each value when multiplied by itself. 
        #whichever product is closest to x or is x we can return as the answer. 

        #if there is no official product that equals x then we return the closest. 

        # we can do binary search, because we are creating a list that is in sorted order.
        
        
        l, r = 0, x
        while l <= r: 
            m = (l + r) // 2
            if (m * m) < x: 
                l = m + 1
            elif (m * m) > x: 
                r = m - 1
            
            else:
                return m

        return r




