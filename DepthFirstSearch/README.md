# Depth-First Search (DFS) Algorithm

## Overview
This section of the repository focuses on the implementation and testing of the Depth-First Search algorithm. DFS is a key algorithm used in graph theory for traversing or searching a tree or graph data structure. It explores as far as possible along each branch before backtracking.

## Implementation Details
- The DFS implementation is found in `DFS.py`.
- It uses recursion to explore nodes, marking each as visited and traversing to unvisited neighbors.
- The `dfs` function accepts a graph and a starting node, returning a set of nodes in the order they were visited.

## Usage
The DFS algorithm can be utilized by importing the `dfs` function and providing a graph and a starting node:

```python
from DFS import dfs

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

result = dfs(graph, 'A')
print(result)
