class Solution:
    def isSafe(self, row, col, board, n):
        durow = row
        dupcol = col

        # upper-left diagonal
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1

        # left row
        row = durow
        col = dupcol
        while col >= 0:
            if board[row][col] == "Q":
                return False
            col -= 1

        # lower-left diagonal
        row = durow
        col = dupcol
        while row < n and col >= 0:
            if board[row][col] == "Q":
                return False
            row += 1
            col -= 1

        return True

    def solve(self, col, board, ans, n):
        if col == n:
            ans.append(board[:])      # copy board
            return

        for row in range(n):
            if self.isSafe(row, col, board, n):
                board[row] = board[row][:col] + "Q" + board[row][col+1:]
                self.solve(col + 1, board, ans, n)
                board[row] = board[row][:col] + "." + board[row][col+1:]


n = 4
board = ["." * n for _ in range(n)]
ans = []

obj = Solution()
obj.solve(0, board, ans, n)

print(ans)

# TC= O(N! * N)
# SC =O(N^2 + N)