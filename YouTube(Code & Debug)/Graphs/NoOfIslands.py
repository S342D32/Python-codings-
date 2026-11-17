from collections import deque

def bfs(i,j,visited,grid,rows,cols):
  queue = deque()
  queue.append((i,j))
  visited[i][j] = 1
  while queue:
    i,j = queue.popleft()
    for x,y in [(-1,0),(1,0),(0,1),(0,-1)]:
      new_i,new_j = x+i,x+j
      if new_i >=0 and new_i < rows and new_j >=0 and new_j < cols and grid[new_i][new_j] =="1" and visited[new_i][new_j] ==0:
        visited[new_i][new_j] = 1
        queue.append((new_i, new_j))

def NoOfIslands(grid):
  count=0
  rows = len(grid)
  cols = len(grid[0])
  visited =[[0 for i in range(cols)] for j in range(rows)]
  for r in range(rows):
    for c in range(cols):
      if grid[r][c] =="1" and visited[r][c] ==0:
        count+=1
        bfs(r,c,visited,grid,rows,cols)
        
  return count

grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]

print(NoOfIslands(grid))
