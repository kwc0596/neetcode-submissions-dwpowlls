class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        l, r = 0, len(numbers) - 1
        

        #we want index1 and index2 to sum up to be the target value. 
        #we also want index1 < index2
        #index1 != index2

        #target - index1 = index2
        

        # two pointers needed for this problem. 
        # One set at beginning of array
        # Other set at the end of the array.
        #iterate until the left pointer is = to or > than r pointer
        while l < r : 
            #We are returning the indices not the values. 
            #We calculate our current sum by taking the value at the beginning and value at the end. 
            #We check to see if the value is higher than the target. If it is, then you will know that we need to find a value that is smaller
            #on the left side of the right pointer. We know this because the array is sorted. 
            #Same goes for if the value is lower than the target. Then you can find a value that is bigger on the right side of the left pointer.
            #for either of these steps, decrement or increment respectively. 
            #if the curSum is equal to the target than we can just return the indice by adding + 1 to both. Why? because 
            curSum = numbers[l] + numbers[r]
            if curSum > target: 
                r -= 1
            elif curSum < target: 
                l += 1
            else: 
                return [l + 1, r + 1]
        return []



