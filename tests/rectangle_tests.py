import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_one_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
    
    def test_both_zero_area(self):
        res = area(0, 0)
        self.assertEqual(res, 0)
       
    def test_rectangle_area(self):
        res = area(10, 20)
        self.assertEqual(res, 200)

    def test_one_zero_perimeter(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 0)
       
    def test_both_first_perimeter(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_area_type_int(self):
        res = area(3, 4)
        self.assertIsInstance(res, int)

    def test_perimeter_type_int(self):
        res = perimeter(3, 4)
        self.assertIsInstance(res, int)

    def test_area_large_numbers(self):
        res = area(10**6, 10**6)
        self.assertEqual(res, 10**12)

    def test_perimeter_large_numbers(self):
        res = perimeter(10**6, 10**6)
        self.assertEqual(res, 4 * 10**6)

    def test_area_fractional_sides(self):
        res = area(2.5, 4.0)
        self.assertAlmostEqual(res, 10.0)

    def test_perimeter_fractional_sides(self):
        res = perimeter(2.5, 4.0)
        self.assertAlmostEqual(res, 13.0)

    def test_area_negative_side(self):
        res = area(-3, 4)
        self.assertEqual(res, 0)

    def test_perimeter_negative_side(self):
        res = perimeter(-3, 4)
        self.assertEqual(res, 0)

    def test_area_one_side(self):
        res = area(1, 100)
        self.assertEqual(res, 100)

    def test_perimeter_one_side(self):
        res = perimeter(1, 100)
        self.assertEqual(res, 202)
