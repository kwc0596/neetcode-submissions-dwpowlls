class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Edge cases... 
        #What about if there's duplicates. I think they can just be ignored, because the goal is a consecutive sequence.
        #No negatives

        #I am thinking about using a HashMap to store values. 

        #could also just sort the entire array. 
        #after sorting, check to see if there are any existing values that are + 1, otherwise return 0. 

        #count the length of the array. So consecutive sequence cannot be greater than length of nums array. 

        


        NumSet = set(nums)

        longest = 0

        
        #We cant to use a conditional that checks to see which values in the array are starter values. This is important since
        #we are looking for consecutive patterns. 
        for n in NumSet:

            if (n - 1) not in NumSet: 
                length = 0
                while (n + length) in NumSet: 
                    length += 1
                longest = max(length, longest)
        return longest
        