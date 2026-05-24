class Solution:
    def mySqrt(self, x: int) -> int:

        l, r = 0, x
        while l <= r: 
            m = (l + r) // 2

            if m * m < x: 
                l = m + 1
            elif m * m > x: 
                r = m - 1
            else: 
                return m
        return r 

        #set up our pointers. if we are trying to find our sqrt of x, then we need to set up pointer from 0 till
        #x value. 

        #while loop while l <= r. 
        #set up midpoint to be sum of pointers // 2. 
        #condition checking if m * m is less than, greater than, or equal to x. 
        #if equal to x, return m value. 
        #otherwise we return r. 
        #we return r because once the while loop breaks, l is no longer the closest number multiplied by itself that is equal to x. 
        #it is going to be the r value . 