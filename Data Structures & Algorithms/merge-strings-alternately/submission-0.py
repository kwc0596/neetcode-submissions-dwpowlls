class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #two pointer problem. i and j will take from word1 and word2 respectively. 

        #set up a while loop that checks to see if i and j are less than len of word1 and word2. 
        #continue to add the characters in alternating order until that is satisfied. 

        #once the condition is no longer satisfied, add the remainder of word1 or word2 to the rest of the string.

        word3 = '' 
        i, j = 0, 0

        while i < len(word1) and j < len(word2): 
            word3 += word1[i]
            word3 += word2[j] 
            i += 1
            j += 1
        while i < len(word1): 
            word3 += word1[i]
            i += 1
        while j < len(word2): 
            word3 += word2[j]
            j += 1
        return word3