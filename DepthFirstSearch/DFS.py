def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=' ')  # Print visited node

    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)

    return visited

# Example graph
graph = {
    'A': ['B', 'C'],  # Node A has neighbours B and C
    'B': ['D', 'E'],  # Node B has neighbours D and E
    'C': ['F'],       # Node C has neighbour F
    'D': [],          # Node D has no neighbours
    'E': ['F'],       # Node E has neighbour F
    'F': []           # Node F has no neighbours
}

# Example usage
dfs_visited = dfs(graph, 'A')  # Starting the DFS from node 'A'
