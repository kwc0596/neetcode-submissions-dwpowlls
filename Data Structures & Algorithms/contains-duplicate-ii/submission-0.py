class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #check if array contains duplicate. 
        #but the duplicates must also have a difference smaller or equal to k

        #array is not sorted

        #not distinct

        #k is any integer greater or equal to 0

        #brute force is while loop that then checks with another while loop if there's a repeating value. 
        #take the difference between the two absolute value it and compare to k


        

        #i think a hashmap can be used here where we store the value as the key and the indice position as the value. 

        dictionary = {}

        for i, num in enumerate(nums) : 
            if num in dictionary and i - dictionary[num] <= k: 
                return True
            dictionary[num] = i
        return False



