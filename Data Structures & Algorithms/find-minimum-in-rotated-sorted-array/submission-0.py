class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0] #start of array where min should technically be.
        l, r = 0, len(nums) - 1 #pointers at far left and far right

        while l <= r: #binary search algorithm
            if nums[l] < nums[r]: #quick end to check if l most is < right most
                res = min(res, nums[l])#can end the loop immediately and get our cur min
                break 
            
            m = (l + r) // 2 #mid point
            res = min(res, nums[m])#checks to see if this value is smaller than current res
            if nums[m] >= nums[l]: #checks to see if m is >= l. if so, then we can remove the left side and just focus on the right.
                l = m + 1
            else: 
                #if other condition is false, we check the left side.
                r = m - 1
        return res 