import unittest
from isTriangle import Triangle
# import sys
# sys.path.append("..")
# from src.Triangle import Triangle

class DecisionCoverageTest(unittest.TestCase):
    def test1(self):
        actual = Triangle.classify(-2, 10, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def test2(self):
        actual = Triangle.classify(6, 6, 7)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test3(self):
        actual = Triangle.classify(6, 9, 6)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test4(self):
        actual = Triangle.classify(4, 9, 9)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test5(self):
        actual = Triangle.classify(3, 4, 6)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

    def test6(self):
        actual = Triangle.classify(2, -2, -2)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test7(self):
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    def test8(self):
        actual = Triangle.classify(2, 3, 6)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()