class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        ROWS, COLS = len(matrix), len(matrix[0]) #Set up the rows and columns
        self.sumMat = [[0] * (COLS + 1) for r in range(ROWS + 1)] #setup the sum matrix but add + 1 to rows and +1 to columns


        for r in range(ROWS): #nested for loop starting with rows
            prefix = 0 #setup prefix variable before going through columns
            for c in range(COLS): 
                prefix += matrix[r][c] #increment prefix variable by adding matrix value at [r][c]
                above = self.sumMat[r][c + 1]
                self.sumMat[r + 1][c + 1] = prefix + above #set up summatrix value by adding +1 to r and +1 to c


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1 #because we are getting these values from summatrix we need to set up r1, c1, r2, and c2 to be + 1

        #formula is bottomRight + topLeft - above - left because we are are only looking for the value inside the selected rectangle
        bottomRight = self.sumMat[row2][col2] #bottomright is the far right corner of the selected value
        above = self.sumMat[row1 - 1][col2] #above is row right above r1 but same column.
        left = self.sumMat[row2][col1 - 1] #left is column to the left of c1 but same row
        topLeft = self.sumMat[row1 - 1][col1 - 1] #topLeft is far left corner 

        return bottomRight - above - left + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)