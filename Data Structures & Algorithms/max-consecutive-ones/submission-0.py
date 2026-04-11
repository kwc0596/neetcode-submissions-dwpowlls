class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
       #this isn't a hashMap. we only need to iterate through the array once. we definitely have to iterate through
       #every number in the array. 

       # i believe we could just set up a cnt variable and increment and then do a max. 
        #we store values to hold our max counter.
        cnt = 0
        current_count = 0
        #iterate through the array.
        for num in nums:
            #if condition checking if the number is 1, add current_count 
            if num == 1: 
                current_count += 1
            else: 
                cnt = max(current_count, cnt)
                #need to reset the current_cnt value.
                current_count = 0
                
        #return max of the current cnt or previous.
        return max(current_count, cnt)


