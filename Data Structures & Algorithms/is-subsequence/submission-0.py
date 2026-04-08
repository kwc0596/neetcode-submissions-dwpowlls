class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #i think a algorithm that can be utilized is to set a rule where a specific character at a specific position
        #cannot be greater than its current position. for example, 'node' the 'o' cannot be in a lower position than 1

        i, j = 0, 0

        while i < len(s) and j < len(t) : 
            if s[i] == t[j]: 
                i += 1
            j += 1
        return i == len(s)