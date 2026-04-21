class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #sort the array in ascending order. 

        #nested loop to .... l pointer starting at 0. r pointer starting at max length of array. 


        #we add two values starting from both l and r. based on whether or not it is greater or less than target,
        #we take the next value from l if it is less than or r if it is greater than? 

        #distinct in that case does not mean duplicate, it just means literally the same value from the same position? 


        n = len(nums)
        result = []
        nums.sort()
        
        for i in range(n): 
            if i > 0 and nums[i] == nums[i - 1]: 
                continue
            for j in range(i + 1, n): 
                if j > i + 1 and nums[j] == nums[j - 1]: 
                    continue
                l = j + 1
                r = n - 1

                while l < r: 
                    current_sum = nums[i] + nums[j] + nums[l] + nums[r]

                    if current_sum == target:
                        result.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]: 
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif current_sum < target: 
                        l += 1
                    else: 
                        r -= 1
        return result

                 

                

