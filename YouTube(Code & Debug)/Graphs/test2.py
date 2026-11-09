

def dfs(node,adj,result,visited):
  visited[node] =1
  result.append(node)
  for node in adj[node]:
    if visited[node] == 0:
       dfs(node,adj,result,visited)
  return result

n =9
result=[]
visited=[0]*(n+1)
adj =[[],[2,8],[1,3,4],[2],[2,5],[4,6],[5,7],[6,8],[1,7,9],[8]]
print(dfs(1,adj,result,visited))

