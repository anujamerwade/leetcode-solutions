class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        row = -1
        col = -1

        notEmpty = True

        # this is to replace r,c from arguments
        for i in range(n):
            for j in range(n):
                if board[i][j] == ".":
                    row = i
                    col = j
                    notEmpty = False
                    break

            # if any empty element remaining in row
            if notEmpty == False:
                break
        # if no empty elements remaining
        if notEmpty == True:
            return True # sudoku is solved

        # backtrack
        for num in range(1, 10):
            if self.isSafe(board, row, col, str(num)):
                board[row][col] = str(num) # might be False
                if self.solveSudoku(board):
                    return True # found answer
                else:
                    board[row][col] = "."
        
        return False



    def isSafe(self, board, row, col, num):
        n = len(board)
    
        # Check if value already present in the row
        for i in range(n):
            if board[row][i] == num:
                return False
            
        # Check if value already present in the column
        for i in range(n):
            if board[i][col] == num:
                return False
        
        # Check if value already present in the 3x3 box
        startRow, startCol = 3 * (row // 3), 3 * (col // 3)
        for i in range(startRow, startRow + 3):
            for j in range(startCol, startCol + 3):
                if board[i][j] == num:
                    return False
            
        return True
