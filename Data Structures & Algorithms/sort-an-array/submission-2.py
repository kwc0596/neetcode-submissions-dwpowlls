class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #We will be using merge sort in this problem. 

        #Merge Sort is a recursive implementation. we will continously call the merge sort function until 
        #the array is reduced to 1. merge sort uses a midpoint to cut the array in half. 
        #the array being reduced to 1 is our base case and is then when we can do the rest of the algorithm. 
        #it does a comparison between the left and right array and used a new empty array to handle our new fully
        #sorted array. 

        def merge_sort(arr) : 
            if len(arr) > 1: 
                mid = len(arr) // 2
                left_arr = arr[:mid]
                right_arr = arr[mid:]


                merge_sort(left_arr)
                merge_sort(right_arr) 

                i, j, k = 0, 0, 0

                while i < len(left_arr) and j < len(right_arr) : 

                    if left_arr[i] < right_arr[j]: 
                        arr[k] = left_arr[i]
                        i += 1
                        
                    else: 
                        arr[k] = right_arr[j]
                        j += 1
                    
                    k += 1
                while i < len(left_arr): 
                    arr[k] = left_arr[i]
                    i += 1
                    k += 1
                while j < len(right_arr):
                    arr[k] = right_arr[j]
                    j += 1
                    k += 1
            return arr
        merge_sort(nums)
        return nums