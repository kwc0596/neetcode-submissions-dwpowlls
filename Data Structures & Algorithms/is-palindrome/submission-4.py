class Solution:
    def isPalindrome(self, s: str) -> bool:
        #We can use a two pointer solution here. How. 
        #How? We can check to see if the l pointer matches the r pointer at each given position. 
        #If it does, then we can increment l and decrement r and continue forward until the pointers intersect each other. 
        #We also need to filter out the capital letters. Because if we do a comparison of 'l' and 'L', they aren't going to be
        #the same, when in this context, they should be. 

        l, r = 0, len(s) - 1 # when doing pointers, the r pointer i believe will have to be the length - 1, because just
        #the length alone would be out of bounds if we were looking at index positions. 

        while l < r: 
            while self.isNotAlphaNum(s[l]) and l < r:
                l += 1
            while self.isNotAlphaNum(s[r]) and l < r: 
                r -= 1
            if s[l].lower() != s[r].lower(): 
                return False
            l += 1
            r -= 1
        return True
            

    def isNotAlphaNum(self, chr): 
        if not( ord('A') <= ord(chr) <= ord('Z') or ord('a') <= ord(chr) <= ord('z') or ord('0') <= ord(chr) <= ord('9')): 
            return True
        return False