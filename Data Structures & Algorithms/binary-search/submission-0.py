class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #we know that the array is sorted. 
        #we also know the exact number that we are looking for. 

        #could we possibly start in the center of the array. check to see whether or not target > mid integer. 


        midpoint = len(nums) // 2
        i = 0
        if nums[midpoint] > target: 
            while i < midpoint: 
                if nums[i] == target: 
                    return i
                i += 1
        else:
            i = midpoint
            while i < len(nums): 
                if nums[i] == target: 
                    return i
                i += 1
        
        return -1
