class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        #If the array are going be sorted in ascending order, in order to find the maximum difference, we just
        #need to look at the first integer of every array and last integer of every array . Between 
        #so it is all coming from one array . an array of arrays. 


        #first time around, for loop to grab the index 0 value in each array. 

        #second time around for loop to grab the index -1 value in each array. 
        #in each iteration, do a comparison between current value -1 and the max. likewise for minimum. 

        #return the absolute difference max - min


        
        

        cur_min, cur_max = arrays[0][0], arrays[0][-1] 
        res = 0

        for i in range(1, len(arrays)): 
            arr = arrays[i]
            res = max(res, arr[-1] - cur_min, cur_max - arr[0])
            cur_min = min(cur_min, arr[0])
            cur_max = max(cur_max, arr[-1])
        return res

