class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #So we want to iterate through the array, and find the longest count that we can until there is a character
        #that repeats itself. 

        #We can iterate through the array and add what we've already iterated to an additional string. we can check
        #to see if that character has already been added. if it has, then we return our current input. 

        #setting up a set to effectively remove duplicates.
        #set up our l pointer 
        #set up our longest result value
        charSet = set() 
        l = 0
        res = 0

        #iterate through array with the r pointer.
        for r in range(len(s)): 
            #nested while loop that checks to see if the new r value already exists in the set. if it does we remove
            #the l pointer value and move it one to the right. We do this until there are no more duplicates.
            while s[r] in charSet: 
                charSet.remove(s[l]) 
                l += 1
            #once we are out of the loop we then add the new r value to the set.
            charSet.add(s[r])
            #we do a comparison between our res and our current max which is the indice distance + 1. It is plus one because this is traversing through indices but length is always plus one.

            res = max(res, r - l + 1) 
            #return res at the end. 
        return res


            
         