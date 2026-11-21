def dfs(curr_node,visited,adj_list,visited_path):
  visited[curr_node] =1
  visited_path[curr_node] =1
  for adj_node in adj_list[curr_node]:
    if  visited[adj_node] ==0:
      x=dfs(adj_node,visited,adj_list,visited_path)
      if x ==True:
         return True
    elif visited_path[adj_node] == 1:
      return True
  visited_path[curr_node] =0
  return False

  

def CycleDetectionInDirectedGraph(V,edges):
  adj_list =[[] for _ in range(V)]
  for u,v in edges:
    adj_list[u].append(v)


  visited=V*[0]
  visited_path=V*[0]
  for i in range(0,V):
    if visited[i] ==0:
      ans = dfs(i,visited,adj_list,visited_path)
      if ans == True:
         return True
  return False



  
V = 6

edges = [
    (5, 2),
    (5, 0),
    (4, 0),
    (4, 1),
    (2, 3),
    (3, 1)
]
print(CycleDetectionInDirectedGraph(V, edges))


# TC=O(V+E)
# SC=O(V+E)