class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Reading this prompt, I immediately think of hashMap, because we can utilize a fast lookup tool. 
        #We can iterate through the entire array and add each value to our hashMap. 

        #iterate through our hashmap checking to see value + 1 is in our hashMap, otherwise skip that value. 
        #set up a counter to see how long the sequence is and hold it. and then do a comparison if it needs to be
        #reset and do a comparison to find the longest sequence. 

        hashMap = {}
        #We just added every value in nums to the hashMap. the key is what we want. Value is irrelevant.
        if len(nums) == 0: 
            return 0
        for i in nums: 
            hashMap[i] = hashMap.get(i, 0) + 1
        #We are going to first iterate through the keys. 
        #After we iterate through keys, we we can set up a nested while loop that will go through a consecutive
        #sequence. This while loop will only trigger if it is the first value in it's consecutive
        #sequence. By doing this, we never are looking for a key that is in the middle
        #and this algorithm also overlooks duplicate values. 
        longest = 1
        for key in hashMap.keys():
            if key - 1 not in hashMap:
                current = key
                current_length = 1 
            

                while current + 1 in hashMap.keys(): 
                    current_length += 1
                    current += 1
                    longest = max(longest, current_length)
        return longest
                
                
                


        

        



        
