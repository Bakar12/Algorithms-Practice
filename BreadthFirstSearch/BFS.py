from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = set([start])
    order_of_visit = []  # List to keep track of the order of visit

    while queue:
        vertex = queue.popleft()
        order_of_visit.append(vertex)  # Add vertex to the list

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return order_of_visit  # Return the list of visited nodes


# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

result = bfs(graph, 'A')  # Starting the BFS from node 'A'
print(result)  # Print the result

