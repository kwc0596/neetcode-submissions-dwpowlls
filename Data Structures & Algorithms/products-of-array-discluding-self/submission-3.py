class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Because it is the smallest number, you can make the deduction that the number in output[i] should be the highest
        #permutation. The same applies for the biggest number. And I think you can root out biggest to smallest in the same way
        #the only complication for this algorithm is if there are negative numbers in the input. 

        #how do you iterate through an array and skip using the value that i is at. 

        #i think this is two pointer. 

        #i think that this is a two pointer problem because you can leave one pointer at the unwanted indice? and have the
        #other pointer iterate through the rest of the array. 


    #prefix[i] * postfix[i] solution ? 

    #iterate through the loop. based on the num, get all multiplicators to the left 
    #and all multiplicators to the right

        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)): 
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1): 
            res[i] *= postfix
            postfix *= nums[i]
        return res



                
                
                
