from collections import deque
def TopologikalsortUsingKahnAlgo(V,edges):
  adj_list = [[] for _ in range(V)]
  for u,v in edges:
    adj_list[u].append(v)
  result =[]
  queue = deque()
  indegree = [0]*V
  for i in range(0,V):
    if indegree[i] ==0:
      queue.append(i)
  while queue:
    curr_node = queue.popleft()
    result.append(curr_node)
    for adj_node in adj_list[curr_node]:
      indegree[adj_node]-=1
      if indegree[adj_node]==0:
        queue.append(adj_node)
  return result




