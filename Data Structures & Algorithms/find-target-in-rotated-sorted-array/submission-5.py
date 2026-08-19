class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #We know it is a binary search problem because the array is technically sorted. It is just rotated. We are
        #looking for the index of nums of a specific number (target) otherwise return -1

        l, r = 0, len(nums) - 1


        while l <= r: 

            mid = (l + r) // 2

            #we need to do two checks. First to determine whether or not to look left or right. 
            if target == nums[mid]: 
                return mid
            
            if nums[mid] >= nums[l]: 

                if target > nums[mid]: #target greater than mid value
                    l = mid + 1
                elif target < nums[l]: #target smaller than l value checking if target < nums[r] is the same condition as target > nums[mid]
                    l = mid + 1
                else: 
                    r = mid - 1
            else: #checks if the target is in the sorted right half.
                if target < nums[mid]: #checks target is less than mid to search to the left
                    r = mid - 1
                elif target > nums[r]: 
                    #checks target is greater than nums[r] to search to the left as well
                    r = mid - 1
                else: 
                    #will search right.
                    l = mid + 1
        return -1
            