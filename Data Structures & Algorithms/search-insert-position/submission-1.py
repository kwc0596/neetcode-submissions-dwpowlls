class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #basically you set up the search insert position the exact same way
        #we would a traditional binary search algorithm. Instead of returning -1,
        #we will return the indice of the last value we are looking at.


        l, r = 0, len(nums) - 1
        
        while l <= r:
            midpoint = (l + r) // 2 
            if nums[midpoint] < target: 
                l = midpoint + 1
            elif nums[midpoint] > target: 
                r = midpoint -  1
            elif nums[midpoint] == target: 
                return midpoint
        if nums[midpoint] < target: 
            return midpoint + 1
        else: 
            return midpoint 
