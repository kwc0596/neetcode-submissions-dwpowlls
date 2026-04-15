class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Because it is the smallest number, you can make the deduction that the number in output[i] should be the highest
        #permutation. The same applies for the biggest number. And I think you can root out biggest to smallest in the same way
        #the only complication for this algorithm is if there are negative numbers in the input. 

        #how do you iterate through an array and skip using the value that i is at. 

        #i think this is two pointer. 

        #i think that this is a two pointer problem because you can leave one pointer at the unwanted indice? and have the
        #other pointer iterate through the rest of the array. 

        i = 0
        res = []
        
        while i < len(nums): 
            j = 0
            permutation = 1
            while j < len(nums): 
                if i == j: 
                    j += 1
                else:
                    permutation *= nums[j]
                    j += 1
            res.append(permutation)
            i += 1
        return res
                
                
                
