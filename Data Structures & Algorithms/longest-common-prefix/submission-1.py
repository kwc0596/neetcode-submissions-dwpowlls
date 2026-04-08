class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #i think we can sort the array. 
        # find the length of shortest string. 
        #check to see if shortest string exists in every other string. 
        # if not continously decrement by 1 and then compare again. 
        # if not found, then return ""
        if not strs: 
            return ""
        
        sortedArray = sorted(strs)
        

        first = sortedArray[0]

        last = sortedArray[-1]



        i = 0

        #create a while loop to check and see if the character at specific index matches the last character as well. 

        #the reason we only need to do a first and last comparison is because lexographic matters in code. and so if 
        #the last string matches the first, you know everything in the middle also does as well. 
        while i < len(first) and i < len(last) and first[i] == last[i]: 
            i += 1
        return last[:i]

