def solve(i, j, a, n, ans, move, vis):
    if i == n - 1 and j == n - 1:
        ans.append(move)
        return

    vis[i][j] = 1

    # Down
    if i + 1 < n and not vis[i + 1][j] and a[i + 1][j] == 1:
        solve(i + 1, j, a, n, ans, move + "D", vis)

    # Left
    if j - 1 >= 0 and not vis[i][j - 1] and a[i][j - 1] == 1:
        solve(i, j - 1, a, n, ans, move + "L", vis)

    # Right
    if j + 1 < n and not vis[i][j + 1] and a[i][j + 1] == 1:
        solve(i, j + 1, a, n, ans, move + "R", vis)

    # Up
    if i - 1 >= 0 and not vis[i - 1][j] and a[i - 1][j] == 1:
        solve(i - 1, j, a, n, ans, move + "U", vis)

    vis[i][j] = 0


def ratMaze(matrix):
    n = len(matrix)
    ans = []
    vis = [[0] * n for _ in range(n)]

    if matrix[0][0] == 1:
        solve(0, 0, matrix, n, ans, "", vis)

    return ans


matrix = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 1, 0],
    [0, 1, 1, 1]
]

ans = ratMaze(matrix)

print(ans)
# Time: O(4^N*2)
# Space: O(N^2)