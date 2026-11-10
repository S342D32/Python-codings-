from copy import deepcopy

def dfs(i,j,new_color,initial_color,visits,rows,cols):
  if i < 0 or i >= rows or j<0 or j >=cols:
    return
  if visits[i][j] != initial_color:
    return
  if visits[i][j] == new_color:
    return
  visits[i][j] = new_color
  dfs(i+1,j,new_color,initial_color,visits,rows,cols)
  dfs(i,j-1,new_color,initial_color,visits,rows,cols)
  dfs(i-1,j,new_color,initial_color,visits,rows,cols)
  dfs(i,j+1,new_color,initial_color,visits,rows,cols)

def flood_fill(image,sr,sc,color):
  if image[sr][sc] == color:
    return image
  visits = deepcopy(image)
  rows = len(visits)
  cols = len(visits[0])
  initial_color=visits[sr][sc]
  dfs(sr,sc,color,initial_color,visits,rows,cols)
  return visits

print(flood_fill([[1,1,1],[1,1,0],[1,0,1]], 1,1,2))