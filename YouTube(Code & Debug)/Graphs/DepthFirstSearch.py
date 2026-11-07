
def dfs(node,result,visited,adj):
  visited[node] =1
  result.append(node)
  for node in adj[node]:
      if visited[node] ==0:
        dfs(node, result, visited, adj)
  return result

n =9
result=[]
visited=[0]*(n+1)
adj =[[],[2,8],[1,3,4],[2],[2,5],[4,6],[5,7],[6,8],[1,7,9],[8]]
print(dfs(1,result,visited,adj))

# TC=O(N)+ O(2E)
# SC=O(2N)(VISIT RESULT)+ O(2E)(Stack space)