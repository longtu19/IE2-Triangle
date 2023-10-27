import unittest
from isTriangle import Triangle
# import sys
# sys.path.append("..")
# from src.Triangle import Triangle

class StatementCoverageTest(unittest.TestCase):
    def test1(self):
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type.EQUILATERAL
        # self.assertEqual(actual, expected)
    
    def test2(self):
        actual = Triangle.classify(6, 4, 7)
        expected = Triangle.Type.SCALENE
        # self.assertEqual(actual, expected)

    def test3(self):
        actual = Triangle.classify(4, 9, 9)
        expected = Triangle.Type.ISOSCELES
        # self.assertEqual(actual, expected)

    def test4(self):
        actual = Triangle.classify(2, -2, -2)
        expected = Triangle.Type.INVALID
        # self.assertEqual(actual, expected)

    def test5(self):
        actual = Triangle.classify(7, 7, 2)
        expected = Triangle.Type.ISOSCELES
        # self.assertEqual(actual, expected)

    def test6(self):
        actual = Triangle.classify(7, 6, 7)
        expected = Triangle.Type.ISOSCELES
        # self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
