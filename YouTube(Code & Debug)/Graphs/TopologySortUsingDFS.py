def dfs(i,stack,visited,adj_list):
  visited[i] =1
  for adj_node in adj_list[i]:
    if visited[adj_node] == 0:
      dfs(adj_node, stack, visited, adj_list)
  stack.append(i)

def TopologySortUsingDFS(V,edges):
  adj_list = [[] for _ in range(V)]
  for u,v in edges:
    adj_list[u].append(v)
  stack=[]
  visited=[0 for _ in range(V)]
  for i in range(0,V):
    if visited[i] ==0:
      dfs(i,stack,visited,adj_list)
  return stack[::-1]


V = 6

edges = [
    (5, 2),
    (5, 0),
    (4, 0),
    (4, 1),
    (2, 3),
    (3, 1)
]

print(TopologySortUsingDFS(V, edges))

# TC=O(V+E)
# SC=O(V+E)