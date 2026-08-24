class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Search a 2D Matrix. We sort of need to incorporate binary search twice here. We know we can use it because the matrix that is being used is already sorted from left to right. When I think of non decreasing order, I think that distinct values are possible. we will first set up our rows and columns. This is necessary in order to traverse through any one of the rows . We can determine from there if target given would even exist in our current matrix. After doing the search for the correct row, we can then use binary search to find out if it exists in that nested array. Return false if it does not. 


        ROWS, COLS = len(matrix) , len(matrix[0]) #I wonder if i need to decrement these lengths by 1...

        top, bot = 0, ROWS - 1

        while top <= bot: 
            
            rows = (top + bot) // 2
            if target < matrix[rows][0]: 
                bot = rows - 1
            elif target > matrix[rows][-1]: 
                top = rows + 1
            else: 
                break #this means we found the row. so no need to stick around.
        
        if not (top <= bot):#we check this in case the reason we get to this condition is because the while loop ended. So either we got here by breaking out of the while loop or we got here because of the loop being finished. 
            return False

        rows = (top + bot) // 2

        l, r = 0, COLS - 1 # it is COLS - 1 because we are setting our bounds to be the starting index of an array (0) and the last pos of an array which is COLS - 1 because in this case it is 0, 1, 2, 3

        while l <= r: 
            m = (l + r) // 2

            if target < matrix[rows][m]: 
                r = m - 1
            elif target > matrix[rows][m]: 
                l = m + 1
            else: 
                return True
        return False