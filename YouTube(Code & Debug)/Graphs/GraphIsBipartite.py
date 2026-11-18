
def dfs(curr_node, visited, graph, color):
    visited[curr_node] = color

    for adjNode in graph[curr_node]:

        if visited[adjNode] == -1:
            ans = dfs(adjNode, visited, graph, 1 - color)

            if ans == False:
                return False

        elif visited[adjNode] == visited[curr_node]:
            return False

    return True


def GraphIsBipartite(graph):
    total_nodes = len(graph)
    visited = [-1] * total_nodes

    for index in range(total_nodes):
        if visited[index] == -1:
            if not dfs(index, visited, graph, 0):
                return False

    return True
graph = [
    [1, 3],
    [0, 2],
    [1, 3],
    [0, 2]
]
print(GraphIsBipartite(graph))