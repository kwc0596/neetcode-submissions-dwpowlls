class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        window = set() #hashset used to account for duplicates

        L = 0 #set up our left pointer

        for R in range(len(nums)): #we are moving through the array with the R pointer
            
            if R - L > k : #checks if the difference of R and L is greater than k. we know the window is too big if this is true so we remove the l indice value from the set and increment L.
                window.remove(nums[L])
                L += 1
            if nums[R] in window: #checks if r indice value exists in our window. if it does we know its within the window and true.
                return True
            window.add(nums[R]) #will add the value of r pointer to the window.
        return False #returns false if we're able to exit the loop without finding a duplicate that is within the window.


