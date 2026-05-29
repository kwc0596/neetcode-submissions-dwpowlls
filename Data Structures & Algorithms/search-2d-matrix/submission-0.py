class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #we kind of want to binary search the matrix. 
        #so our pointers in this case would be first row and lowest row? 

        #because we are checking to see if the target integer exists inside of the matrix. 
        ROWS, COLS = len(matrix), len(matrix[0])

        top = 0
        bot = ROWS - 1

        while top <= bot: 
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]: 
                bot = row - 1
            else: 
                break 
        if not (top <= bot)  : 
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

