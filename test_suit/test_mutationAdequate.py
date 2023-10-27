import unittest
from isTriangle import Triangle
# import sys
# sys.path.append("..")
# from src.Triangle import Triangle

class MutationCoverageTest(unittest.TestCase):
    def test1(self):
        actual = Triangle.classify(10, 1, 10)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)



if __name__ == '__main__':
    unittest.main()