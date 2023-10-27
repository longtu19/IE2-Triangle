import unittest
from isTriangle import Triangle
# import sys
# sys.path.append("..")
# from src.Triangle import Triangle

class MutationCoverageTest(unittest.TestCase):
    def test1(self):
        actual = Triangle.classify(8, 1, 8)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test2(self):
        actual = Triangle.classify(4, 4, 2)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test3(self):
        actual = Triangle.classify(3, 6, 6)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test4(self):
        actual = Triangle.classify(12, 3, 3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test5(self):
        actual = Triangle.classify(0, 1,1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test6(self):
        actual = Triangle.classify(3, 4,5)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

    def test7(self):
        actual = Triangle.classify(9, 4,5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test8(self):
        actual = Triangle.classify(2, 2,4)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test9(self):
        actual = Triangle.classify(2, 4,2)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test10(self):
        actual = Triangle.classify(4, 2,2)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test11(self):
        actual = Triangle.classify(1, 2,2)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
    
    def test12(self):
        actual = Triangle.classify(1, 1,1)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    def test13(self):
        actual = Triangle.classify(1, 1,0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test14(self):
        actual = Triangle.classify(3, 5,8)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test15(self):
        actual = Triangle.classify(3, 8,5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test16(self):
        actual = Triangle.classify(5, 0,5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
if __name__ == '__main__':
    unittest.main()