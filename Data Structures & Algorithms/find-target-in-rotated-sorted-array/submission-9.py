class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r: 

            #check if l pointer is less than r pointer. 
            #then we have an idea of whether or not array is sorted. 
            mid = (l + r) // 2
            if nums[mid] == target: 
                return mid
            
            
            if nums[mid] >= nums[l]: 
                if target < nums[l]: #check if target < nums[l] to search right
                
                    l = mid + 1
                elif target > nums[mid]: 
                    l = mid + 1
                else: 
                    r = mid - 1
            
            else: #this condition would be if nums[mid] < nums[l] 
                #right side
                if target > nums[r]: 
                    r = mid - 1
                elif target < nums[mid]: 
                    r = mid - 1
                else: 
                    l = mid + 1
        return -1