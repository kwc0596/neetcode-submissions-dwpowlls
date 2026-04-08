class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
         
        #in neetcode's solution, he iterates through the array from the last indice. 
        #the reason he does is this is because we are already told what the last value is going to be. -1.
        #We have a starting point that we can use, and then just continuously do a comparison between the values
        #there are two temp values that we are to continously replace. 

        rightMax = -1

        for i in range(len(arr) - 1, -1, -1): 
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        return arr
