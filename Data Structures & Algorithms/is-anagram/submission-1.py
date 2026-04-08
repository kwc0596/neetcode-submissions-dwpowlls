class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        


        #We're just keeping track of the characters

        #create a hashset for both strings
        #then check if hashset 1 is equivalent to hashset 2? 

        hashS = {} 
        hashT = {} 

        for i in s: 
            hashS[i] = hashS.get(i, 0) + 1
        
        for i in t: 
            hashT[i] = hashT.get(i, 0) + 1

        if hashT == hashS: 
            return True
        return False