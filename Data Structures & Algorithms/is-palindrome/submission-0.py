class Solution:
    def isPalindrome(self, s: str) -> bool:
        #can set up a left and right pointer
        #because we are only looking for alphanumeric values, we want to check to see if the character is alphanumeric. 
        #create another function to check if that is the case by finding out the charater's ordinance value
        #set up two while loops to see if the value is alphanumeric and also want to account for the pointer whether right or left to be decremented or incremented
        # check to see if the value at the left pointer matches the value at the right pointer. Return the boolean value. 

    
        l, r = 0, len(s) - 1

        while l < r: 
            while l < r and not self.isAlphaNum(s[l]): 
                l += 1
            while r > l and not self.isAlphaNum(s[r]): 
                r -= 1
            if s[l].lower() != s[r].lower(): 
                return False
            l += 1
            r -= 1
        return True
            #while character at left position is not alphanumeric, increment pointer. We also want to make sure that left is still less than right
            #if l pointer is equal to right pointer but also that it is lowercase? 

            #same thing for right pointer 

            #check to see if lowercase version is not the same as right pointer. if not return false 

            #after doing the comparison, increment and decrement both pointers.
    




    # This function will pull the ordinance value of the character string and determine if it is one of the values within the alphabet or numbers 0 - 9
    def isAlphaNum(self, c): 
        return (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9') )



