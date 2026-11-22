
from collections import deque

def CycleDetectionInDirectedGraphKahnAlgo(V, edges):
    adj_list = [[] for _ in range(V)]

    for u, v in edges:
        adj_list[u].append(v)

    indegrees = [0] * V

    # Calculate indegree
    for u, v in edges:
        indegrees[v] += 1

    queue = deque()

    for i in range(V):
        if indegrees[i] == 0:
            queue.append(i)

    result = []

    while queue:
        curr_node = queue.popleft()
        result.append(curr_node)

        for adj_node in adj_list[curr_node]:
            indegrees[adj_node] -= 1

            if indegrees[adj_node] == 0:
                queue.append(adj_node)

    # If all nodes are not processed, cycle exists
    if len(result) != V:
        return True

    return False


V = 4
edges = [[0, 1], [0, 2], [1, 3], [2, 3]]
print(CycleDetectionInDirectedGraphKahnAlgo(V, edges))

