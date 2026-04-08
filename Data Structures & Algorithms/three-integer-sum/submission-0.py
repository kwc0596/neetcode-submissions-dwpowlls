class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #two pointers, but three poitners in this case? 

        #set l to left of array, j to mid array, and k to end. 

        #sort the array. 

        # find the sum of i, j, and k. if the target is too large, shift k pointer to left. if too small shift left pointer to the right. 
        
            
        res = [] #create an empty array, since we are returning a list of sequences that equal 0.
        nums.sort() #sort the nums array so that we can easily skip duplicates

        for i, a in enumerate(nums): #enumerate for loop for i, a in enumerate(nums): 
            if i > 0 and a == nums[i - 1]: # check to see that the position is not starting position and also value is not a duplicate 
                continue # carry on otherwise this whole thing would be skipped if it was a duplicate
            l, r = i + 1, len(nums) - 1 #set up our two pointers, left at starting i + 1, rright pointer all the way at end.
            while l < r: #set up whil loop so that l never passes r pointer
                threeSum = a + nums[l] + nums[r] #set up our threesum variable that is the sum of a + nums[l] + nums[r]
                if threeSum > 0: #conditional that checks if threeSum is greater than 0. we need to make it smaller so decrement r pointer
                    r -= 1 #because the list is sorted we know that we will get a smaller value
                elif threeSum < 0: #conditional that checks if threeSum is less than 0. We need to make it bigger so increment l pointer
                    l += 1 #increments because we know list is sorted
                else: 
                    res.append([a, nums[l], nums[r]]) #else condition where we know threeSUm equals 0. we can append into our current res array.
                    l += 1 #increment l by 1 because we want to move over to our next 
                    while nums[l] == nums[l - 1] and l < r: 
                        l += 1
        return res
    #    set up an empty result array which takes the three values. 
    #    sorting the array makes this a whole lot easier

    # we want to capture both the index and the value so that means we need to do an enumerate step . 
    # if the value of a is greater than 0 we break because it doesn't make sense to continue the loop. 
    #the target value is supposed to be 0 so if every value starting from first is positive, there's no point in continuing the loop. 
    # we are also checking for duplicates. if i > 0 meaning its not in the first position and the next value is also equal to a , we skip this value
    # since we do not want duplicates. 
    # left pointer is set to i + 1 because it should be the value after a or if i + 1 is a duplicate we move it along. r would be set to the value at
    # the end of the array. 
    # set up a while look that checks if l < r 
    # setup our current threesum. calculate a + nums[l] + nums[r] 
    # setup our conditional statements. if threesum > 0 , move r to the left. 
    # if threesum < 0 , move l to the left
    # if threesum == 0, append the values to the result array. 
    # we're not done here since we also want to pull in any other DISTINCT combinations. 
    # we also need to increment and decrement l and r respectively. 
    # we also want to set up another while loop that checks to see if nums[l] == nums[l - 1] to scan for additional duplicates. we would continously 
    #increment l. the reason we don't set up the same condition for r pointer is because a is fixed. if l is different, then even if r is the same, you
    #wouldn't get the correct answer. 
    # now we can just return result. 
    #
    