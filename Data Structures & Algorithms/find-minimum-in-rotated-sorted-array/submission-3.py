class Solution:
    def findMin(self, nums: List[int]) -> int:
        #the rotation I believe does not matter with the algorithm. we are using binary search in this case. 
        #it is appropriate because we're looking for the minimum value in a sorted array. if it wasn't sorted, I do
        #not think that binary search would be appropriate. 

        #set up pointers. 
        l, r = 0, len(nums) - 1

        res = nums[0]

        while l <= r: 

            if nums[l] <= nums[r]: 
                res = min(nums[l], res)

                return res
            
            m = (l + r) // 2

            res = min(nums[m], res)

            if nums[m] >= nums[l]: 
                l = m + 1
            else: 
                r = m - 1
        return res
