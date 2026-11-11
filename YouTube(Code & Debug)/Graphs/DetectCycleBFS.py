from collections import deque

def DetectCycle(V,edges):
  adj_list =[[] for _ in range(V)]
  for u,v in edges:
    adj_list[v].append(u)
    adj_list[u].append(v)
  visited =[0] *V
  for i in range(V):
    if visited[i] ==1:
      continue
    queue = deque()
    queue.append((i,-1))
    visited[i]=1
    while queue:
      node,parent=queue.popleft()
      for adjnode in adj_list[node]:
        if visited[adjnode] ==0:
          visited[adjnode] =1
          queue.append((adjnode,node))
        else:
          if adjnode != parent:
            return True
  return False

  
# TC =O(N+2E)
# SC =O(N+N)
V = 5

edges = [
    [0, 1],
    [1, 2],
    [2, 0],
    [3, 4]
]

print(DetectCycle(V, edges))


        



  