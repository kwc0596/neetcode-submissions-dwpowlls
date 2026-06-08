class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        res = nums[0] #we set it to the first number in the array just in case it is already sorted. this is
        #where the minimum value is technically supposed to be. 

        while l <= r:

            if nums[l] < nums[r]: 
                #we know array is sorted if this is true. 
                res = min(res, nums[l])
                break #break immediately since we know we found the lowest integer. 

            
            m = (l + r) // 2

            res = min(nums[m], res) 

            if nums[m] >= nums[l]: 
                l = m + 1
            else: 
                r = m - 1
        return res