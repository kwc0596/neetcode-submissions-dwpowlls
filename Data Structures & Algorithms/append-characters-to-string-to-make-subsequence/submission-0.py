class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        #We should find the commonalities between the two strings. look at s and see
        #when it no longer matches str t in the indx.

        #a subsequence is a string that can be derived from another string by deleting
        #some or no characters without changing the order of the remaining characters. 

        #if none of the characters exist in s, we would then need to append the entire
        #t string for t to be a subsequence of s. 

        #in the case if the entire t exists already in s, the output would be 0.

        # I am thinking that the two pointer algorithm is the best solution

        # we can iterate with a for loop and check each string at the same time until
        #there is not a match. 

        i, j = 0, 0
        while i < len(s) and j < len(t): 
            #this loop will continue while both conditions are applicable. if either
            #one of these reach the end of the string, there is no point in continuing. 
            #we can set up an if condition that checks if both characters at an indice
            #are the same. if they are, we can continue and increment both indices. 
            #if they are not the same, we can return the length of our output. 

            if s[i] == t[j]: 
                i += 1
                j += 1
            else: 
                i += 1
        return len(t) - j
