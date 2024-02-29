class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        result = []
        self.nqueens(board, 0, n, result)
        return result

    def nqueens(self, board, row, n, result):
        if row == n:
            result.append(["".join(row) for row in board])
            return
        for col in range(n):
            if self.isSafe(board, row, col, n):
                board[row][col] = 'Q'
                self.nqueens(board, row + 1, n, result)
                board[row][col] = '.'

    def isSafe(self, board, row, col, n):
        # check vertical
        for r in range(row):
            if board[r][col] == 'Q':
                return False
        
        # check upper left diagonal
        r, c = row, col
        while r > 0 and c > 0:
            r -= 1
            c -= 1
            if board[r][c] == 'Q':
                return False
        
        # check upper right diagonal
        r, c = row, col
        while r > 0 and c < n - 1:
            r -= 1
            c += 1
            if board[r][c] == 'Q':
                return False
        
        return True
