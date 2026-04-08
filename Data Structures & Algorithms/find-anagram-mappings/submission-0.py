class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #The mappings array mirrors nums1. because the indice in the mappings array is saying that 
        #the number in nums1 is going to be at THIS index position in nums 2. 

        #So I think a hashmap would be the best.

        i, j = 0, 0
        mappings = []

        while i < len(nums1): 
            #iterate through nums 1. each iteration, we stop and search through nums2 for the same number and then 
            #mark the location in mappings array. 
            while j < len(nums2): 
                if nums1[i] !=  nums2[j]: 
                    j += 1
                else: 
                    mappings.append(j)
                    j = 0
                    break
            i += 1
        return mappings