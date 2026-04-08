class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #set up rows
        #set up columns

        #since it is a 9 x 9 board, then 9 rows, and 9 columns. Not 10 because we're not using 0s
        # (0,0) , (2, 2) should contain 1 - 9 values. same for (3, 3) , (5, 5) , same for (6, 6) (8,8)

        #set up our hashmaps to hold set values. the reason we are using sets is because we want to prevent duplicate values. 

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9): 

                #first thing we want to do is check for edge cases, in this case,  empty values which are treated with ."

                if board[r][c] == '.': 
                    continue
                
                #next we want to look for duplicate values. so we check to see if current value at board[r][c] is in our row, col, or 
                #squares hashset. 

                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r // 3, c // 3)]): 
                    return False
                
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True