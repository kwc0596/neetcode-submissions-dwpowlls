class Solution:
    def validPalindrome(self, s: str) -> bool:
        #a palindrome is a string that reads the same forward and backward. It also means 
        #that if the string is odd counted, the characters need to show up an equal amount except for one character
        #if a string is odd, each character needs to show up an even amount of times. 

        #so we would normally check to see if l pointer and r pointer indice are equal. if they aren't we would immediately
        #return false. in this case, we can move the pointer over by one and do another comparison. if that still doesn't work we can
        #do the opposite by going back. if we originally decrement r and compared new r to old l, now we can increment 
        #l to compare new l to old r. if that still doesn't work, then we can return false, other continue incrementing. 


        l, r = 0, len(s) - 1
        def is_palindrome(l, r): 
            while l < r: 
                if s[l] != s[r]: 
                    return False
                l += 1
                r -= 1
            return True

        while l < r: 
            while l < r and self.isNotAlphaNum(s[l]): 
                l += 1
            while l < r and self.isNotAlphaNum(s[r]):
                r -= 1
            if s[l] != s[r]: 
                return (is_palindrome(l + 1, r) or 
                        is_palindrome(l, r - 1))
            l += 1
            r -= 1
        return True






    def isNotAlphaNum(self, c): 
        if not(ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z') or ord('0') <= ord(c) <= ord('9')): 
            return True
        else: 
            return False

