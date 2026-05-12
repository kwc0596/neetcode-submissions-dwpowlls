class Solution:
    def isValid(self, s: str) -> bool:
        #a string we are given only can contain these characters: () {} []
        #will only be considered valid if it is closed by the opposite string. 

        #I think we can check the string character append each parntheses character that appears to a 
        #new array. 
        #if we find a ), }, or ], we can pop the value. 

        #for loop to iterate through s. 

        #check to see if ch is }
        #if prev ch is {, then pop

        #i think we only need to append opening to the new array. 
        #we can pop when the closing appears. 

        
        #create a dictionary that attaches each open bracket to its respective closing bracket

        #We want to iterate through the array UNTIL we find a closed bracket. because if the array is legitimate, the
        #first closing bracket that we arrive at should have the correct open bracket directly to the left of it.
        #once we find that first one, we can pop that open one from the array. 

        openToClose = {')': '(', '}': '{', ']': '['}
        stack = []

        for ch in s: 
            if ch in openToClose: 
                if stack and stack[-1] == openToClose[ch]: 
                    stack.pop()
                else: 
                    return False
            else: 
                stack.append(ch)
        return True if not stack else False
                

