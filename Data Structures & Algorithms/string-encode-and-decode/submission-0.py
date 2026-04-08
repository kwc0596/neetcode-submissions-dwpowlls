class Solution:

    def encode(self, strs: List[str]) -> str:

        #use an empty string variable to combine the string list into one. 
        #use an integer number to determine length of the string a delimiter # 
        res = ""
        for s in strs: 
            res += (str(len(s)) + "#" + s)
        
        return res

    def decode(self, s: str) -> List[str]:

        res = [] 

        i = 0

        while i < len(s): 
            j = i 

            while s[j] != "#": 
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length]) 
            i = j + 1 + length
        
        return res
