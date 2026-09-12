class Solution:
    def solve(self, col, board, ans, n, leftrow, lowerDiag, upperDiag):
        if col == n:
            ans.append(board[:])
            return

        for row in range(n):
            if leftrow[row] == 0 and lowerDiag[row + col] == 0 and upperDiag[n - 1 + col - row] == 0:

                board[row] = board[row][:col] + "Q" + board[row][col+1:]

                leftrow[row] = 1
                lowerDiag[row + col] = 1
                upperDiag[n - 1 + col - row] = 1

                self.solve(col + 1, board, ans, n, leftrow, lowerDiag, upperDiag)

                board[row] = board[row][:col] + "." + board[row][col+1:]

                leftrow[row] = 0
                lowerDiag[row + col] = 0
                upperDiag[n - 1 + col - row] = 0

    def solveNQueens(self, n):
        ans = []
        board = ["." * n for _ in range(n)]

        leftrow = [0] * n
        lowerDiag = [0] * (2 * n - 1)
        upperDiag = [0] * (2 * n - 1)

        self.solve(0, board, ans, n, leftrow, lowerDiag, upperDiag)
        return ans


obj = Solution()
print(obj.solveNQueens(4))