class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #Two pointers. 
        # I think that we can start a pointer at the beginning of the string.
        # The second pointer can start at the end of the string. 

        # probably use a while loop where we keep iterating until the pointers are the same or pass each other? 

        l, r  = 0, len(s) - 1

        while l < r: 
            s[l], s[r] = s[r], s[l]

            l += 1
            r -= 1
        
    
