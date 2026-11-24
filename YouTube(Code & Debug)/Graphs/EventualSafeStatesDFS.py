def dfs(curr_node,visit,path_visit,graph,is_safe,v):
  visit[curr_node]=1
  path_visit[curr_node]=1
  for adj_node in graph[curr_node]:
    if visit[adj_node]==0:
      ans=dfs(adj_node, visit, path_visit, graph, is_safe, v)
      if ans==False:
        return False
      elif path_visit[adj_node] ==1:
        return False
  is_safe[curr_node]=1
  path_visit[curr_node]=0
  return True


def EventualSafeStatesDFS(graph):
  v = len(graph)
  adj_list =[[] for _ in range(v)]
  visit=[0] * v
  path_visit=[0] * v
  is_safe=[0] * v
  for i in range(v):
    if visit[i]==0:
      dfs(i,visit,path_visit,graph,is_safe,v)
  result =[]
  for i in range(v):
    if is_safe[i]== 1:
      result.append(i)
  return result


graph = [[1, 2], [3], [3], []]

print(EventualSafeStatesDFS(graph))

