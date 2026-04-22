class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #with a rotation implementation, it makes me think of using a hashMap. For a hashmap, we can 
        #store the original index position as the value. and with k , we can add k to every index so we get our
        #new index position for each integer. 

        #but with a two pointer, how could we do this... 


        hashMap = {} 

        for i in range(len(nums)): 
            hashMap[nums[i]] = i + k
        #so we just iterated through the entire array and stored the new index position of each integer. 

        #so now we need to think about how to deal with integers that go out of bounds and get pushed to the beginning
        #of the array. so for those, I am thinking we would need to take the length of the array and subtract the new position
        #value. if the value is negative then we know it is out bounds. the new difference is it's new position. abs value.
        #if k is a really large number we want to think about what would have to happen if a number goes through the array
        #multiple times. so after a diff = length - new position. if that diff is STILL a negative number abs value it and subtract
        #from length again until it is less than length. that diff is our new position. 
        length = len(nums)
        for number, index in hashMap.items(): 
            if index < length: 
                nums[index] = number
            else:
                diff = index % length
                nums[diff] = number
        return nums


        