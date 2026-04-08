class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(nums):
            if len(nums) < 2: 
                return nums
            
            mid = len(nums) // 2
            left = merge(nums[:mid])
            right = merge(nums[mid:])

            return merge_sort(nums, left, right)



    




        def merge_sort(nums, left, right):
            i = j = 0
            result = []
            while i < len(left) and j < len(right):
                if left[i] < right[j]: 
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            
            if i < len(left): 
                result.extend(left[i:])
            if j < len(right):
                result.extend(right[j:])

            return result
        return merge(nums)