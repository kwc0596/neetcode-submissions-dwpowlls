class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #If you cannot use the same element twice, that immediately tells me we should use some type of set. This 
        #will help us remove the duplicates in the array.
        #This is a 1-indexed array. 

        #HashMap here for sure, we need the value and index to set the answer. 

        #The key can be the indice and the value can be the integer. 

        #Since the solution must use O(1) additional space, now I am thinking about two pointers


        # we want to set up a brand new array that will hold the result. 

        #iterate through the array with two pointers a left and right. 
        #set up a difference variable that is target - numbers[i]. if that value is the
        #right pointer we can return the two indices. 

        l, r = 0, len(numbers) - 1

        while l < r:
            #We can use this implementation since we know that this is sorted. 
            current_sum = numbers[l] + numbers[r] 

            if current_sum == target: 
                return [l + 1, r + 1]
            elif current_sum < target: 
                l += 1
            else: 
                r -= 1
            
            