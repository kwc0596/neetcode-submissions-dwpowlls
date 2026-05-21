class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #we know that the array is sorted. 
        #we also know the exact number that we are looking for. 

        #could we possibly start in the center of the array. check to see whether or not target > mid integer. 


        l, r = 0, len(nums) - 1

        while l <= r: 
            m = (l + r) // 2
            if nums[m] > target: 
                r = m - 1
            elif nums[m] < target: 
                l = m + 1
            else: 
                return m
        
        return -1
