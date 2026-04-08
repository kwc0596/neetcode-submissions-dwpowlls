class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #The mappings array mirrors nums1. because the indice in the mappings array is saying that 
        #the number in nums1 is going to be at THIS index position in nums 2. 

        #So I think a hashmap would be the best.
        #Since we know that num2 is us looking for the index position. 
        hashing = {}
        for i, n in enumerate(nums2): 
            hashing[n] = i

        mapping = []

        for num in nums1: 
            mapping.append(hashing[num])
        
        return mapping






