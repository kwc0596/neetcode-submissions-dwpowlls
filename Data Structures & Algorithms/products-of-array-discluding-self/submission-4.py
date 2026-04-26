class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #I believe for this problem, what can be done is finding the product of every value before the self integer
        #and then also the product of every value after the self integer. 

        #for this instance, we could use a hashMap to store those multiplicators of the before and after.


        #for example, we can iterate through the array. and the prefix Multiplicator for the first integer would be 1. 
        #for the postFix multiplicator it would be everything after.

        #We will iterate through the array twice. the first time to find the prefix.

        output = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1) : 
            output[i] *= postfix
            postfix *= nums[i]
        return output


