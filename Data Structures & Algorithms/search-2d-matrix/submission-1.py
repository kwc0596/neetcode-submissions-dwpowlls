class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #we know that the matrix is sorted. 
        #we can do a double binary search. 
        #the first search would be to check which row the target WOULD sit in
        #if it actually exists. 

        #the second binary search is to track down if the target actually does
        #exist. We are actually finding it. 

        #we can define our rows and columns. 

        ROWS, COLS  = len(matrix) , len(matrix[0])

        #we want to define our pointers. 
        top, bot = 0, ROWS - 1

        while top <= bot: 
            row = (top + bot) // 2
            if target > matrix[row][-1]: 
                top = row + 1
            elif target < matrix[row][0]: 
                bot = row - 1
            else: 
                break 
        if not (top <= bot): 
            return False
        
        row = (top + bot) // 2

        l, r = 0, COLS - 1

        while l <= r: 
            m = (l + r) // 2
            if target > matrix[row][m]: 
                l = m + 1
            elif target < matrix[row][m]: 
                r = m - 1
            else: 
                return True
        return False