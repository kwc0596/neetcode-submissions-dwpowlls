class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hashMap
        #key will be the number. 
        #value will be the amount of times it is populated. 

        #sort the array first 
        
        frequentHash = {} 
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums: 
            frequentHash[n] = 1 + frequentHash.get(n, 0)
        
        for n, c in frequentHash.items(): 
            freq[c].append(n)


        result = [] 

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i] : 
                result.append(n) 
                if len(result) == k: 
                    return result

        