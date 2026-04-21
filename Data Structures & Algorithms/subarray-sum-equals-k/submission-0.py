class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #res holds the value we want to return that keeps track of the total number of subarrays which sum equals to k

        res = 0

        #curSum takes the value of our current iteration and increments based off the values we have already seen

        curSum = 0

        #prefixSums stores the possible prefix sums and how often they appear in the array
        prefixSums = { 0: 1 } 

        #iterate through nums array
        for n in nums: 
            #increment curSum by adding the values
            curSum += n
            #take the difference of current Sum and subtract by k to get the leftover
            diff = curSum - k

            #if that leftover (potential prefix Sum) is already in our hash table, add
            #that number to our result.

            res += prefixSums.get(diff, 0) 
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

        return res