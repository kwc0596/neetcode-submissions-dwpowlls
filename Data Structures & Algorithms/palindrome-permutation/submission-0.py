class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        #So in order to check for this, we will need to rearrange the letters..
        #I think hashing is also good because we would have a count of each letter.
        #so a palindrome reads the same forward and backward. meaning there needs to be an equal number of the same letters
        #except for the middle letter.
        #actually even numbered palindromes do exist, but in that case every character must appear an even number of times. 

        hashMap = {} 
        cnt = 0

        for i in range(len(s)): 
            hashMap[s[i]] = hashMap.get(s[i], 0) + 1

        if len(s) % 2 == 0: 
            #If the string is even, i want to check to see if every character appears an 
            #even amount of times. so I could iterate through the hashmap with the key
            #and value or maybe just the value, and see if every single value is divisible
            #by 2. if it is, then we know it can be a palindrome. 
            #otherwise, return false

            for value in hashMap.values(): 
                if value % 2 != 0: 
                    return False
            return True

        
        if len(s) % 2 != 0: 
            #so if the string is odd, we can check if every character appears an even amount
            #of times EXCEPT for one character. one character should appear just once or an odd amount of times?

            for value in hashMap.values(): 
                if value % 2 != 0: 
                    cnt += 1
                if cnt > 1:
                    return False
            return True
