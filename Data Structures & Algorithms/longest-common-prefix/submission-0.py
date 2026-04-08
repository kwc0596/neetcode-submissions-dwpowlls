class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #iterate through the array. 
        #check what is shortest string is. We can base the algorithm around that. 
        # check to see if shortest string is in remaining strings.
        # make that str shorter by one character each time. 

        #sort the array based off shortest string
        #iterate through the array to see if shortest string is in other strings. 
        #if it is, then that's our prefix.
        #otherwise, if it doesn't apply for remaining strings, remove one character.

        #Assuming that the first string in the array is the shortest string. 
        #We can then assume that that is the longest possible prefix in the array. 
        #We can initialize an empty string which the end result will be our prefix 
        #Because we are using the first string in the array as our longest possible prefix, we can calculate the length of 
        #that string and iterate through it with i

        #we are going through each character at index and comparing to make sure that each character matches to proceed with the prefix
        # Create nested for loop that iterates through each string in strings array
        #In order to do that, we need to create a nested loop that does an edge case check
        #One edge case is to check if the length of that string is the same as I. If it is you know you reached your limit and need to return
        #res where it is. 
        #2nd edge case is to check if current string is not equal to first string at position i. if its not equal then you know that they're different and
        #return res where its currently at. 

        #In outer for loop, we will add first string's character based on position i to res string. 

        #return res outside of loop 

        res = ''

        for i in range(len(strs[0])): 
            for s in strs: 
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            
            res += strs[0][i]
        
        return res
