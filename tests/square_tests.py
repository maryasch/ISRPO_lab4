import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
       
    def test_square_area(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
       
    def test_first_perimeter(self):
        res = perimeter(30)
        self.assertEqual(res, 120)

    def test_area_type_int(self):
        res = area(7)
        self.assertIsInstance(res, int)

    def test_perimeter_type_int(self):
        res = perimeter(7)
        self.assertIsInstance(res, int)

    def test_area_large_number(self):
        res = area(10**6)
        self.assertEqual(res, 10**12)

    def test_perimeter_large_number(self):
        res = perimeter(10**6)
        self.assertEqual(res, 4 * 10**6)

    def test_area_fractional_side(self):
        res = area(2.5)
        self.assertAlmostEqual(res, 6.25)

    def test_perimeter_fractional_side(self):
        res = perimeter(2.5)
        self.assertAlmostEqual(res, 10.0)

    def test_area_negative_side(self):
        res = area(-5)
        self.assertEqual(res, 0)

    def test_perimeter_negative_side(self):
        res = perimeter(-5)
        self.assertEqual(res, 0)

    def test_area_one(self):
        res = area(1)
        self.assertEqual(res, 1)

    def test_perimeter_one(self):
        res = perimeter(1)
        self.assertEqual(res, 4)
