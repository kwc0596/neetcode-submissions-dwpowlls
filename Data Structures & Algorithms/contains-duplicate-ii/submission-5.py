class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        #we are using a hashSet to add every value that goes through this array. 

        #if we find that after moving the R pointer continously to the right makes the L value out of bounds where it is also a duplicate, we remove that value from the hash Set. 
        #the second condition checks to see if the indice is in the hashSet. then we know that it is a duplicate value. We can return True since we know that it is within the sliding window. 


        window = set() 

        L = 0 #set up L pointer and only L pointer for now. 

        for R in range(len(nums)): #iterate through nums with the R pointer. It has to check every value in the array including nums[0] otherwise if we skip over it, that value will never be included in the array. 
            
            #first condition checks if window is out of bounds. If it does not, we can remove the L pointer value
            #from the hashset and increment L.
            if R - L > k: 
                window.remove(nums[L])
                L += 1
            
            
            #second condition checks if value exists inside of our hash set
            if nums[R] in window: 
                return True

            
            
            


            #add R pointer value to the hashset
            window.add(nums[R])
        return False