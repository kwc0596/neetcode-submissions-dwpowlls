class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #no hashMaps

        #set up i and j pointers. 

        #nested loop where we start at index 0. and j will be equal to i + 1
        i = 0
        while i < len(numbers): 
            difference = target - numbers[i]
            j = i + 1
            while j < len(numbers): 
                if numbers[i] == numbers[j]: 
                    continue
                elif numbers[j] == difference: 
                    return [i + 1, j + 1]
                j += 1
            i += 1

                