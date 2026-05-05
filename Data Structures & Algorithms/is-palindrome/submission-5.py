class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        #two pointer solution. 
        #iterate from front and end. 
        #check to see if characters at l and r are alphanumerical. if they are not, increment until they are. once
        # they both are, check to see if they are the same. 
        #if they are not return false.
        #return true at end of loop. 

        while l < r : 
            while l < r and self.isNotAlphaNum(s[l]): 
                l += 1
            while l < r and self.isNotAlphaNum(s[r]): 
                r -= 1
            if s[l].lower() != s[r].lower(): 
                return False
            l, r = l + 1, r - 1
        return True

            



    def isNotAlphaNum(self, c): 
        if not (ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z') or ord('0') <= ord(c) <= ord('9')):
            return True
        else: 
            return False