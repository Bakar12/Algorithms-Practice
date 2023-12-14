import unittest
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from LinearSearch import linearSearch

class TestLinearSearch(unittest.TestCase):
    def test_linear_search(self):
        arr = [2, 3, 4, 10, 40]  # Input array
        x = 10  # Element to search for
        expected_output = 3  # Expected output index
        
        result = linearSearch(arr, x)  # Call the linearSearch function
        
        self.assertEqual(result, expected_output)  # Check if the result matches the expected output

if __name__ == '__main__':
    unittest.main(exit=False)  # Run the unit tests
