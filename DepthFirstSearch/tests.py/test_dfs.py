import unittest
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the DFS function from the DFS module
from DFS import dfs

class TestDFS(unittest.TestCase):
    
    def setUp(self):
        # Define the graph for testing
        self.graph = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': [],
            'E': ['F'],
            'F': []
        }

    def test_dfs(self):
        # Define the start node and expected output
        start_node = 'A'
        expected_output = {'A', 'B', 'D', 'E', 'F', 'C'}  # The order can vary
        
        # Call the dfs function and compare the result with the expected output
        result = dfs(self.graph, start_node)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    # Run the unit tests
    unittest.main()
