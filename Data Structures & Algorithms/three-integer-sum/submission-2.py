class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #target is essentially 0. 

        #no duplicate triplets, butdoubles seem to be okay. if target is essentially 0 what we can likely do is set up 
        #a value where we are only looking for a sum between integers 1 and integers 2. or maybe we should take the sum 
        #of two numbers and if it is smaller than 0 we should look for a larger number. if it is larger than 0, we should look for
        #smaller/negative number. 


        # i think a hashMap would be good here because we could look up values immediately but we would be sacrificing 
        #space efficiency. ... 

        #sort the array. . 



        sortedArr = sorted(nums) 

        res = []

        #we can find a solution with three sum by iterating through the array with two pointers. 
        #the solution will have a nested loop because in the first instance for integer a, that will start at the
        #very beginning of the array. where l will start 1 position over and r will start at the end. with l and r
        #you can then treat it like two sum where if the solution is too big, decrement r and if the solution is too
        #small, decrement l. 

        #Initiates our pointers. a is created and doesn't move in the inner loop. only the outer. 
        


        for i, a in enumerate(sortedArr):
            if i > 0 and a == sortedArr[i - 1]:
                continue

            l, r = i + 1, len(sortedArr) - 1
            while l < r: 
                ans = a + sortedArr[l] + sortedArr[r]
                if ans > 0: 
                    r -= 1
                elif ans < 0: 
                    l += 1
                else: 
                    res.append([a, sortedArr[l], sortedArr[r]])
                    l += 1
                    while sortedArr[l] == sortedArr[l - 1] and l < r: 
                        l += 1
        return res
            
                

                

