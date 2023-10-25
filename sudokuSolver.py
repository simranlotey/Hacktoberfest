class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def isValid(board, row, col, c):
            for i in range(9):
                if board[i][col] == c:
                    return False
                if board[row][i] == c:
                    return False
                row_index = 3 * (row // 3) + i // 3
                col_index = 3 * (col // 3) + i % 3
                if board[row_index][col_index] == c:
                    return False
            return True

        def solve(board):
            for row in range(9):
                for col in range(9):
                    if board[row][col] == ".":
                        for c in range(1, 10):
                            if isValid(board, row, col, chr(c + ord("0"))):
                                board[row][col] = chr(c + ord("0"))
                                if solve(board):
                                    return True
                                else:
                                    board[row][col] = "."
                        return False
            return True

        solve(board)

