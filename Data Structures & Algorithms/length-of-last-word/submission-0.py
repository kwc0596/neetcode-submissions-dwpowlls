class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #so this I believe would also be two pointer. if we just need to return the length of the last word, iterate
        #from the very end. check to see if the first ch in the string is a space. make an exception there but 
        #after that every space that appears after will indicate that you went through the last word. 
        #to detect if a value is a string, i believe we can just check to see if the ch space is alpha numeric. if it is
        #not, we know it is a space. 

        cnt = 0
        for i in range(len(s) -1, -1, -1): 
            if self.isNotAlphaNum(s[i]) and cnt == 0:
                continue
            
            else: 
                if self.isNotAlphaNum(s[i]): 
                    return cnt
                cnt += 1
                
        return cnt
            

    


    def isNotAlphaNum(self, character): 
        if not(ord('a') <= ord(character) <= ord('z') or ord('A') <= ord(character) <= ord('Z')):
            return True
        return False
