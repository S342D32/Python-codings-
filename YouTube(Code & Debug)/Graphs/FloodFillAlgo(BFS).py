from copy import deepcopy
from collections import deque


def flood_fill(image,sr,sc,color):
  if image[sr][sc] == color:
    return image
  visits = deepcopy(image)
  rows = len(visits)
  cols = len(visits[0])
  initial_color=visits[sr][sc]
  queue = deque()
  queue.append((sr, sc))
  while queue:
    i,j = queue.popleft()
    visits[i][j] = color
    for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
      new_i,new_j= i+x , j+y
      if new_i < 0 or new_i >= rows or new_j<0 or new_j>= cols:
        continue
      if visits[new_i][new_j] != initial_color:
        continue
      queue.append((new_i,new_j))
  return visits

print(flood_fill([[1,1,1],[1,1,0],[1,0,1]], 1,1,2))