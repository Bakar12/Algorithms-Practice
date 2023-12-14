import unittest
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from BFS import bfs

class TestBFS(unittest.TestCase):
    def test_bfs(self):
        # Define the graph
        graph = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': [],
            'E': ['F'],
            'F': []
        }
        start_node = 'A'
        expected_output = ['A', 'B', 'C', 'D', 'E', 'F']
        
        # Call the bfs function and get the result
        result = bfs(graph, start_node)
        
        # Check if the result matches the expected output
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    # Run the tests
    unittest.main(exit=False)
