# Breadth-First Search (BFS) Algorithm

## Overview
This section of the repository showcases an implementation of the Breadth-First Search algorithm. BFS is crucial for traversing or searching trees and graphs, starting from a selected node and exploring all adjacent nodes level by level.

## Implementation
- **File**: `BFS.py`
- **Method**: Uses a queue for organized traversal.
- **Functionality**: `bfs(graph, start)` takes a graph and a start node, returning a list of nodes in the order visited.

## Usage
```python
from BFS import bfs

graph = {
    'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'],
    'D': [], 'E': ['F'], 'F': []
}
print(bfs(graph, 'A'))  # Outputs the BFS traversal from node 'A'
