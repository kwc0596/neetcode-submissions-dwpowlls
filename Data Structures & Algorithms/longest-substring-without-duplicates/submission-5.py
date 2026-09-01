class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #longest substring without duplicate characters. 
        #can set up a hashset to check for duplicate characters.

        seen = set() 
        res = 0
        #two pointer aproach?

        L = 0

        for R in range(len(s)): 
            

            while s[R] in seen: 
                seen.remove(s[L]) #remove the first string value
                L += 1 #move l one over to slide the window
            
            seen.add(s[R])
            res = max(res, R - L + 1)
        return res
            



