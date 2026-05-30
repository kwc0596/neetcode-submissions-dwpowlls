class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # do you then determine what the maximum is based off of the highest weight
        #in the array? if so, then you can come with some type of algorithm to find
        #if that weight can be shipped off in the given amount of days. 

        #however, you also have to ship the packages in order. 

        #so the first thing to do would be to sort the array. 


        #i think finding the sum of the array and dividing by days doesn't automatically
        #give you a response because it has to be shipped in order. 

        l, r = max(weights), sum(weights) #pointers. lower bound is the max weight. we can't have a weight capacity that is lower than one of our weights in the array.
        res = r #our current stored result that holds our current acceptable value to return.. 

        def canShip(cap) : #helper function that passes cap parameter.
            ships, currCap = 1, cap #just another form of days, weight capacity.
            for w in weights: #iterate through weights array.
                if currCap - w < 0: #check if current stored cap - w is lower than 0.
                    #this means we will have to add another day (ships += 1)
                    ships += 1
                    currCap = cap #once we add another day, we can reset the weight capacity since it is a new day.
                currCap -= w #decrement current cap by the iterated weight.
            return ships <= days #if number of days(ships) is <= given days return True, otherwise False
        
        while l <= r: #start binary search with 
            cap = (l + r) // 2 
            if canShip(cap): #check if this boolean is true.
                res = min(res, cap)
                r = cap - 1
            else: 
                l = cap + 1
        return res

        