class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #with the smallest space complexity possible, this calls for a two pointer solution.. 

        #completely forgot the sorting algorithms.. 

        #we can set up i and j to start from the beginning and do a comparison between i and j. 

        #so if i is less than j, don't swap. if i is greater than j, then do a swap. 


        #or do a double while loop. j is inside nested loop and goes through the entire array. looking for the
        #smallest value. once the smallest value is found, it does a swap with i if it is smaller than i. 
        #then move i over to the next integer and repeat. 


            def merge(arr, L, M, R):
                left, right = arr[L:M+1], arr[M+1:R+1]
                i, j, k = L, 0, 0

                while j < len(left) and k < len(right):
                    if left[j] <= right[k]:
                        arr[i] = left[j]
                        j += 1
                    else:
                        arr[i] = right[k]
                        k += 1
                    i += 1

                while j < len(left):
                    arr[i] = left[j]
                    j += 1
                    i += 1

                while k < len(right):
                    arr[i] = right[k]
                    k += 1
                    i += 1

            def mergeSort(arr, l, r):
                if l >= r:
                    return
                m = (l + r) // 2
                mergeSort(arr, l, m)
                mergeSort(arr, m + 1, r)
                merge(arr, l, m, r)

            mergeSort(nums, 0, len(nums) - 1)
            return nums
        
