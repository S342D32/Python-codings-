
from collections import deque

def eventualSafeStates(graph):
    v = len(graph)

    adj_list = [[] for _ in range(v)]

    # Reverse the graph
    for node in range(v):
        for adj_node in graph[node]:
            adj_list[adj_node].append(node)

    indegrees = [0] * v

    # Calculate indegree in reversed graph
    for node in range(v):
        for adj_node in adj_list[node]:
            indegrees[adj_node] += 1

    queue = deque()

    for node in range(v):
        if indegrees[node] == 0:
            queue.append(node)

    result = []

    while queue:
        curr_node = queue.popleft()
        result.append(curr_node)

        for adj_node in adj_list[curr_node]:
            indegrees[adj_node] -= 1

            if indegrees[adj_node] == 0:
                queue.append(adj_node)

    result.sort()
    return result


graph = [[1, 2], [3], [3], []]

print(eventualSafeStates(graph))


# Time: O(V+E+Vlog V), including sorting.
# Space: O(V+E)