class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums)) 
        #initialize our result array to have values of 1
        prefix = 1
        #set up prefix to be 1
        for i in range(len(nums)): 

            #for loop to iterate through entire nums array
            #replace result array at index i to be prefix value
            
            res[i] = prefix
            #we increment prefix by multiplying it but the next position in nums array.
            prefix *= nums[i]
        #outside of the first for loop initialize postfix
        postfix = 1
        for i in range(len(nums) - 1, -1, -1): 
            #in our second for loop we are iterating from the end to the beginning.
            #replace result array at index i to multiply current value by current postfix
            #increment postfix by multiplying it by the next position in nums array.
            res[i] *= postfix
            postfix *= nums[i]
        #return the results array.
        return res