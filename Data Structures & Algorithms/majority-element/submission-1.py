class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        #Given an array nums of size n, return the majority element. 
        # The majority element is the element that appears more than n/2 times in the array. You may assume that the majority elemtn always
        # exists in the array. 


        #When I think of problems where you have to do a comparison within an array, that sounds like a hashmap problem. 
        #Let's go ahead and create an empty hashmap. 

        count = {}


        #We also have to find a majority element. That means we can use the max method. But we want to use two variables to store these numbers
        # So we can create two variables, one that stores the final result, and the one that keeps the high max at that moment. 

        res, maxCount = 0, 0

        #We can increment through the array, and store the number in the hashmap as the key. Each time it gets added to the hashmap that would be
        #the count which is the 'value'. 
        # We can then do an if condition that sets our result to that value if it is higher than the maxCount. If it isn't then result is just
        # result in that case. It doesn't change. 
        for n in nums: 
            count[n] = 1 + count.get(n, 0)
            res = n if count[n] > maxCount else res
            maxCount = max(maxCount, count[n])
        return res
        
        # We want to do a maxCount comparison after this where we check if the max is either our current max or the current hashed value.

        #Iterating through the loop afterwards at the very end outside of the loop we will return res. 
        
        