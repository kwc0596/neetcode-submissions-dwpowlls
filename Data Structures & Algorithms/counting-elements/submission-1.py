class Solution:
    def countElements(self, arr: List[int]) -> int:
        #Because we are keeping track of the count of elements in the array, I immediately think of a hashMap. 

        #we have to iterate through the entire array at least once. this is guaranteed. 
        #duplicates are to be counted separately. 

        #basically we're just checking to see if the condition is satisfied. but its all under one variable pretty
        #much? 

        #we are not sorting here. 

        #checking to see if a condition is satisfied, if it is add + 1 to the total count and return. 


        # i need to see a duplicate example because i don't really understand that portion. .. 

        #now I am thinking go back to hashmap

        hashMap = {} 
        #iterate through the array and store the count of each array.
        for i in range(len(arr)): 
            hashMap[arr[i]] = hashMap.get(arr[i], 0) + 1

        cnt = 0
        for num in arr: 
            if (num + 1) in hashMap: 
                cnt += 1
                hashMap[num] -= 1
        
        return cnt

