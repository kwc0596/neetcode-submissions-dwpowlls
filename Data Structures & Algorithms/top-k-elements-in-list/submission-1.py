class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #so k is just the number that you keep to figure out how many numbers are being returned
        #if k is 1, you return the highest appeared element. 
        #if k is 2, you return the two highest.

        #hashMap to count frequency of the characters in the array. 


        #iterate through the values of the hashmap

        hashMap = {} 

        for i in range(len(nums)): 
            hashMap[nums[i]] = hashMap.get(nums[i], 0) + 1

        
        #we're not returning the value though. it would be the key. 

        #use a while loop to iterate until we reduce k to 0?
        
        res = []
        

        sorted_items = sorted(hashMap.items(), key=lambda x: x[1], reverse=True) #sorts by frequency
        i = 0
        while k > 0: 
            res.append(sorted_items[i][0])
            k -= 1
            i += 1
        return res

