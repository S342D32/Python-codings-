def dfs(r,c,r_base,c_base,shape,visited,grid,rows,cols):
  visited[r][c]=1
  shape.append((r-r_base, c-c_base))
  for x,y in [(-1,0),(1,0),(0,1),(0,-1)]:
    new_i,new_j = x+ r,y+c
    if new_i <0 or new_i>= rows or new_j <0 or new_j >= cols:
      continue
    if grid[new_i][new_j] == "1" and visited[new_i][new_j] == 0:
      dfs(new_i, new_j, r_base, c_base, shape, visited, grid, rows, cols)

def NoOfDistinctIslandDFS(grid):
  rows = len(grid)
  cols = len(grid[0])
  visited = [[0 for _ in range(cols)] for _ in range(rows)]
  unique_islands=set()
  for r in range(rows):
    for c in range(cols):
      if grid[r][c] == "1" and visited[r][c] ==0:
        shape=[]
        dfs(r,c,r,c,shape,visited,grid,rows,cols)
        unique_islands.add(tuple(shape))
  return len(unique_islands)


grid = [
    ["0","0","0","0","0","0"],
    ["0","1","1","0","0","0"],
    ["0","0","1","0","0","0"],
    ["0","0","0","1","1","0"],
    ["0","0","1","0","0","0"],
    ["0","0","0","0","0","0"]
]

print(NoOfDistinctIslandDFS(grid))

