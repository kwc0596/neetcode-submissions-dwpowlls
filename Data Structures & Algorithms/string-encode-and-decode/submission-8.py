class Solution:

    def encode(self, strs: List[str]) -> str:
        #encode should get the length of each string and concatenate the strings with a number and hashtag value. 
        #doing this allows us to immediately recognize the number of characters in the string and prevents issues
        #if a hashtag itself is in the word. 
        #so iterate through the strs list, and each str concatenate to new string.
        #edge case if dummy input returns nothing
        

        res = ""

        
        for string in strs: 
            length = str(len(string))
            res += length + "#" + string

        return res


    def decode(self, s: str) -> List[str]:
        #decode should be able to get the length of each individual string, and convert the concatenated
        #string into a list again.
        res = []
        i = 0
        while i < len(s): 
            j = i #start of the number
            while s[j] != '#': 
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j + 1 + length
        return res
             #only the digits before #
            #now j is a '#', so the string starts at j + 1
            #and has length characters
            #append s[j + 1] : j + 1 + length] to result
            # then set i = j + 1 + length
            