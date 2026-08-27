class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #integer array contains non-distinct arrays. 
        #not sorted
        #find two distinct indices where the values at those indices are equal. 
        seen = set() 


        L = 0

        for R in range(len(nums)):
            
            if R - L > k: #window is too big
                seen.remove(nums[L]) #remove the value from the set.
                L += 1
            
            if nums[R] in seen: #checking if r pointer value is already in seen because then we know there's a duplicate. the condition above is done first to remove a value that is out of bounds in the window 
                return True
            
            seen.add(nums[R])

        return False

        #R is the one that is leading the traversal through the array. Not L

            

