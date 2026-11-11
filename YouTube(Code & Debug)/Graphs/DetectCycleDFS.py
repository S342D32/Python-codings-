def dfs(node,parent,visited,adj_list):
  visited[node]=1
  for adjNode in adj_list[node]:
    if visited[adjNode] ==0:
      ans = dfs(adjNode, node, visited, adj_list)
      if ans == True:
        return True
      else:
        if adjNode !=parent and visited[adjNode] ==1:
          return True
  return False




def DetectCycleDFS(V,edges):
  adj_list =[[] for _ in range(V)]

  for u,v in edges:
    adj_list[v].append(u)
    adj_list[u].append(v)
  visited =[0] * V
  for i in range(V):
    if visited[i] ==1:
      continue
    if dfs(i,-1,visited,adj_list) ==True:
      return True
  return False

V = 5

edges = [
    [0, 1],
    [1, 2],
    [2, 0],
    [3, 4]
]

print(DetectCycleDFS(V, edges))