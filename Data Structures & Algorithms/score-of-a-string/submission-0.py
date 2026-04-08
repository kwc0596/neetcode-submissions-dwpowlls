class Solution:
    def scoreOfString(self, s: str) -> int:
        #two pointer? 

        #hash map? 

        #store the value of each ch in hash map? 

        #i think two pointer just because we're looking at the relationship between characters and their adjacent characters

        l, r = 0, 1

        #set up while loop to loop until  we go out of bounds  so.. until l is out of bounds. when r goes out of boudsn
        #we know, that l should be at the last character in the string.? 
        sum = 0
        while r < len(s): 
            diff = abs((ord(s[r]) - ord(s[l])))
            sum += diff

            l += 1
            r += 1
        return sum

    