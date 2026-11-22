from collections import deque

# only return the result instead of true or false
def CourseScheduleKahnsAlgo2(V, edges):
    adj_list = [[] for _ in range(V)]

    for u, v in edges:
        adj_list[v].append(u)
    indegrees = [0] * V

    # Calculate indegree
    for u, v in edges:
        indegrees[u] += 1

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

    # IAll courses can be completed.
    if len(result) == V:
        return result
    # cycle exists
    return []


V = 4
edges = [[0, 1], [0, 2], [1, 3], [2, 3]]
print(CourseScheduleKahnsAlgo2(V, edges))
