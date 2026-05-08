class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #with three indices, we can take have l be the indice far to the right, j to the position right after l,
        #and r at the end of the array. 
        #we need to sort the array to check for duplicates.

        # we will create a res variable to have an empty array. we will append triplets to this array. 
        #for loop enumerate that sets up the first integer and then we will check for duplicates values
        #after i > 0. 
        #set up a while loop to continue while l < r
        #if the sum is greater than 0, decrement r because value is too large. if too small increment l. 
        #if we find a triplet, set up a nested loop that checks if next l is equal to current l to root out duplicates.


        res = [] 
        i = 0
        nums.sort()
        for i, a in enumerate(nums): 

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r: 
                if a + nums[l] + nums[r] > 0: 
                    r -= 1
                elif a + nums[l] + nums[r] < 0: 
                    l += 1
                else: 
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
