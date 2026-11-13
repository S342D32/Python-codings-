def dfs(r,c,rows,cols,matrix,visited):
  if r<0 or r>= rows or c<0 or c>=cols:
     return 
  if matrix[r][c]== "X":
     return
  if visited[r][c] ==1:
     return
  visited[r][c]=1
  dfs(r-1,c,rows,cols,matrix,visited)
  dfs(r+1,c,rows,cols,matrix,visited)
  dfs(r,c-1,rows,cols,matrix,visited)
  dfs(r,c+1,rows,cols,matrix,visited)
  


def SurroundedRegionsProblem(matrix):
  rows = len(matrix)
  cols = len(matrix[0])
  visited = [[0 for _ in range(cols)] for _ in range(rows)]
  for r in range(rows):
     for c in range(cols):
       if r==0 or c==0 or r == rows-1 or c == cols-1:
         if matrix[r][c] =="O":
           if visited[r][c]==0:
              dfs(r,c,rows,cols,matrix,visited)
  for r in range(rows):
     for c in range(cols):
        if matrix[r][c]=="O" and visited[r][c] == 0:
           matrix[r][c] ="X"
  return matrix



matrix = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"]
]

result = SurroundedRegionsProblem(matrix)

for row in result:
    print(row)

# TC = O(N+M) +O((N+M)*4) + O(N*M) = O(N*M)
# SC = O(N*M)
