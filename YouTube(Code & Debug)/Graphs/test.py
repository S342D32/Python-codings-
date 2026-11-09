from collections import deque

def bfs(n,adj,start_node):
  ans=[]
  queue = deque()
  visited = [0]*(n+1)
  queue.append(start_node)
  visited[start_node] =1
  while len(queue)!=0:
    e=queue.popleft()
    ans.append(e)
    for node in adj[e]:
      if visited[node]==0:
        queue.append(node)
        visited[node]=1
  return ans

n =9
adj =[[],[2,8],[1,3,4],[2],[2,5],[4,6],[5,7],[6,8],[1,7,9],[8]]
print(bfs(n,adj,1))
  
