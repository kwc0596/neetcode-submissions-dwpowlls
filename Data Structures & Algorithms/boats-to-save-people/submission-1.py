class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #two pointer problem
        #lower bound set to 0.
        #upper bound set to length of array. 

        #set up a counter to return at the end. 

        #sort the array. 

        #we are going to place the heaviest people in boats first, but still check to see if the lowest weight
        #person can also fit. If they can we can both decrement the right pointer and increment the left pointer. 

        l, r = 0, len(people) - 1

        boats = 0

        people.sort()

        while l <= r: 

            remain = limit - people[r]

            r -= 1

            boats += 1

            if l <= r and remain >= people[l]: 
                l += 1
        return boats



