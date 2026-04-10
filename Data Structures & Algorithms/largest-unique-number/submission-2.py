class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        #Immediately I think hashMap here. I think a hashMap is the best route because, we are keeping count of the 
        #entire array. Or maybe max comparisons? I think HashMap because we need to track frequency. 

        #set up an empty hashMap. 
        #iterate through the entire array and append the values.

        #i think we need to use hashMap because we have to iterate through the entire array. 

        hashMap = {} 

        maxValue = -1

        for num in nums:  
            hashMap[num] = hashMap.get(num, 0) + 1
            #The reason this conditional doesn't work is it is checking the last number and if it is not appearing once, it immediately returns -1.
        #The reason this iteration works is because you can predefine maxValue before iteration
        #You're not using it to search within the hashMap and so you can compare that current value
        #to the values you pull from the hashMap since you're no longer indexing.
        for key, freq in hashMap.items(): 
            if freq == 1:
                maxValue = max(maxValue, key)
        

        #how do i return the largest number with frequency 1.

        
        return maxValue

        # we cannot return until after we have iterated through the entire array.