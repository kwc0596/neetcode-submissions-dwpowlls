class Solution:
    #So I think in the encoding process, we would want to put some kind of marker
    #on the first and last character of each string so that we know where the string
    #starts and stops.
    #that way it is encoded and gets passed to the decode function, we know where
    #to break it apart.
    def encode(self, strs: List[str]) -> str:

        #get the length of each string, add a delimiter #. 
        # when we break it back down we are checking the length of each
        #string so we know to skip over a # if it is in the string. 
        msg = ""
        
        for s in strs: 
            msg += str(len(s)) + "#" + s
        return msg




    def decode(self, s: str) -> List[str]:
        
        i = 0
        listed = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            j += 1
            listed.append(s[j:j+length])
            i = j + length
        return listed