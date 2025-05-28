import unittest
from sort import sort

class TestSort(unittest.TestCase):
    def test_standard_package(self):
        # Test case for standard package
        result = sort(10, 10, 10, 10)
        self.assertEqual(result, 'STANDARD')

    def test_standard_package_different_dimensions(self):
        # Test case with different dimensions
        result = sort(20, 15, 10, 5)
        self.assertEqual(result, 'STANDARD')

    def test_special_package_bulky(self):
        # Test case for bulky package (volume > 1000000)
        result = sort(100, 100, 100, 10)
        self.assertEqual(result, 'SPECIAL')

    def test_special_package_heavy(self):
        # Test case for heavy package (mass > 20)
        result = sort(10, 10, 10, 25)
        self.assertEqual(result, 'SPECIAL')

    def test_special_package_exceeds_dimension(self):
        # Test case for package exceeding any dimension (150cm)
        result = sort(160, 10, 10, 10)
        self.assertEqual(result, 'SPECIAL')

    def test_rejected_package_bulky_and_heavy(self):
        # Test case for package that is both bulky and heavy
        result = sort(100, 100, 100, 25)
        self.assertEqual(result, 'REJECTED')

    def test_rejected_package_dimension_and_heavy(self):
        # Test case for package that exceeds dimension and is heavy
        result = sort(160, 10, 10, 25)
        self.assertEqual(result, 'REJECTED')

    def test_edge_case_maximum_standard(self):
        # Test case for package at the maximum allowed dimensions and weight
        result = sort(99, 99, 99, 19)
        self.assertEqual(result, 'STANDARD')

if __name__ == '__main__':
    unittest.main() 