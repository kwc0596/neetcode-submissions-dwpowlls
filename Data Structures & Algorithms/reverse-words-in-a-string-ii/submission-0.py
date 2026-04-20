class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        

        self.reverse(s, 0, len(s) - 1)


        self.reverse_each_word(s)

    def reverse(self, reversedS, l, r): 

        while l < r: 
            reversedS[l], reversedS[r] = reversedS[r], reversedS[l]
            l += 1
            r -= 1
    
    def reverse_each_word(self, l: List[str]) -> None: 
        n = len(l) 
        start = end = 0

        while start < n: 
            # go to the end of the word
            while end < n and l[end] != " ": 
                end += 1
            #reverse the word
            self.reverse(l, start, end - 1)
            #move to the next word
            start = end + 1
            end += 1


