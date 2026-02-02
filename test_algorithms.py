import unittest
from algorithms import binary_search, bubble_sort

class TestAlgorithms(unittest.TestCase):

    def test_binary_search(self):
        # Test finding an element
        arr = [1, 3, 5, 7, 9]
        self.assertEqual(binary_search(arr, 3), 1)
        self.assertEqual(binary_search(arr, 9), 4)

        # Test element not found
        self.assertEqual(binary_search(arr, 2), -1)
        self.assertEqual(binary_search(arr, 10), -1)

        # Test empty list
        self.assertEqual(binary_search([], 3), -1)

        # Test single element list
        self.assertEqual(binary_search([5], 5), 0)
        self.assertEqual(binary_search([5], 3), -1)

    def test_bubble_sort(self):
        # Test standard sort
        arr = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(bubble_sort(arr), expected)

        # Test already sorted
        arr = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(bubble_sort(arr), expected)

        # Test reverse sorted
        arr = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(bubble_sort(arr), expected)

        # Test empty list
        self.assertEqual(bubble_sort([]), [])

        # Test single element
        self.assertEqual(bubble_sort([1]), [1])

        # Test duplicates
        arr = [3, 1, 3, 2, 1]
        expected = [1, 1, 2, 3, 3]
        self.assertEqual(bubble_sort(arr), expected)

if __name__ == '__main__':
    unittest.main()
