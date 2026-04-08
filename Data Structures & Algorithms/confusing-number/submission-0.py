class Solution:
    def confusingNumber(self, n: int) -> bool:
        #set up a dictionary that store that values of confusing digits. 
        #digits that are invalid should not be stored in the dictionary. 
        #so if a number has an invalid digit , we can automatically return false. 

        #we also need to be aware of the rotation. So for numbers with mulitple digits that would be considered valid,
        #we have to think about placement. the first digit index then becomes the last and so on so forth. 

        #we can also ignore leading 0s. 
        #In order to return true, we also need to know that it is a different number from the original.
        digitMap = {'0': '0', '1' : '1', '6': '9', '8': '8', '9': '6'} 
    
        nString = str(n)
        res = ''
        for i in range(len(nString) - 1, -1, -1): 
            if nString[i] not in digitMap:
                return False
            res += digitMap[nString[i]]
        
        newNum = int(res)

        if newNum != n: 
            return True
        return False
            
            
            