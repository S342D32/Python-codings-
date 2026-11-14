from collections import deque
# BFS Method
def NoOfEnclaves(matrix):
  rows = len(matrix)
  cols= len(matrix[0])
  visited=[[0 for _ in range(cols)] for _ in range(rows)]
  queue = deque()
  for r in range(rows):
      for c in range(cols):
         if r == 0 or  c == 0 or r==rows-1 or c==cols-1:
            if matrix[r][c] == 1:
               queue.append((r,c))
               visited[r][c]=1
  while queue:
     i,j = queue.popleft()
     for x,y in [(-1,0),(0,-1),(0,1),(1,0)]:
        new_i,new_j = i+x, j+y
        if new_i < 0 or new_i >= rows or new_j <0 or new_j >= cols:
           continue
        if matrix[new_i][new_j] == 0:
           continue
        if matrix[new_i][new_j] == 1 and visited[new_i][new_j] == 1:
           continue
        visited[new_i][new_j] = 1
        queue.append((new_i,new_j))
  count =0
  for r in range(rows):
      for c in range(cols):
         if matrix[r][c] == 1 and visited[r][c] == 0:
            count+=1
  return count         


# DFS Method
# def dfs(r,c,visited,grid,rows,cols):
#   if r <0 or r>=rows or c<0 or c>=cols:
#     return
#   if visited[r][c] ==1 and grid[r][c] ==1:
#     return
#   if grid[r][c] ==0:
#     return
#   visited[r][c] =1
#   dfs(r+1, c, visited, grid, rows, cols)
#   dfs(r, c+1, visited, grid, rows, cols)
#   dfs(r-1, c, visited, grid, rows, cols)
#   dfs(r, c-1, visited, grid, rows, cols)


# def noOfEnclaves(grid):
#   rows = len(grid)
#   cols = len(grid[0])
#   visited = [[0 for i in range(cols)] for j in range(rows)]
#   for r in range(rows):
#     for c in range(cols):
#       if r ==0 or c ==0 or r == rows-1 or c == cols-1:
#         if grid[r][c] == 1 and visited[r][c] == 0:
#           dfs(r, c, visited, grid, rows, cols)
#   count =0
#   for r in range(rows):
#       for c in range(cols):
#         if grid[r][c] == 1 and visited[r][c] == 0:
#           count +=1
#   return count

matrix=[[0,0,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,0,0]]
print(NoOfEnclaves(matrix))

# TC = O(N+M) +O((N+M)*4) + O(N*M) = O(N*M)
# SC = O(N*M)
