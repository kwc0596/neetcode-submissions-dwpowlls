class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #is it better to sort this array. 



        #max people per boat is two. we want to prioritize putting heavy because there is only a limit of 2 people
        #per boat.

        people.sort() 
        res = 0
        l, r = 0, len(people) - 1

        while l <= r: #need to include the less than or equal to because we are checking each person one by one.

            remain = limit - people[r]
            r -= 1
            res += 1

            if l <= r and remain >= people[l]: 
                l += 1

        return res 

