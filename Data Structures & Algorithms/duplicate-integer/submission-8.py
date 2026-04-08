class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # set up a hash table to track the cnt of each integer in the array

        #use a for loop to iterate through the entire array and add cnt value for each integer appears

        #check to see if cnt > 1 to return true; 
        #otherwise return false.

        table  = {} 

        for i in nums: 
            table[i] = table.get(i, 0) + 1
            if table[i] > 1: 
                return True
        return False