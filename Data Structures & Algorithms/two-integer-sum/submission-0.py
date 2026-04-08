class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #So we can take the difference of target and each indice in the array by iterating through. 
        #if that difference matches another indice in the array, we know that that output sum will be the target
        #To use a hash map in this context , the key would be the indice, and the value would be the difference after
        #subtracting from target. So we can store the value inside of the hashmap and check to see

        hashMap = {} 

        #after setting up a hashmap, we can then do a for loop with enumerate. 
        for i, n in enumerate(nums) : 

            difference = target - n 

            if difference in hashMap: 
                return [hashMap[difference], i]
            
            hashMap[n] = i 


        #go through real time and figure out the difference. 
        #check to see if that difference is in the hashmap. then we know that we found our two values.
        #return the two indices afterwards.