import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_side_zero_area(self):
        res = area(0, 10)
        self.assertEqual(res, 0)

    def test_height_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
    
    def test_both_zero_area(self):
        res = area(0, 0)
        self.assertEqual(res, 0)
       
    def test_triangle_area(self):
        res = area(10, 20)
        self.assertEqual(res, 100)

    def test_one_zero_perimeter(self):
        res = perimeter(10, 20, 20)
        self.assertEqual(res, 50)
       
    def test_both_first_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_area_type_float(self):
        res = area(3, 4)
        self.assertIsInstance(res, float)

    def test_perimeter_type_int(self):
        res = perimeter(3, 4, 5)
        self.assertIsInstance(res, int)

    def test_area_large_numbers(self):
        res = area(10**6, 10**6)
        self.assertEqual(res, 5 * 10**11)

    def test_perimeter_large_numbers(self):
        res = perimeter(10**6, 10**6, 10**6)
        self.assertEqual(res, 3 * 10**6)

    def test_area_fractional_values(self):
        res = area(2.5, 4.0)
        self.assertAlmostEqual(res, 5.0)

    def test_perimeter_fractional_values(self):
        res = perimeter(2.5, 3.5, 4.0)
        self.assertAlmostEqual(res, 10.0)

    def test_area_negative_side(self):
        res = area(-3, 4)
        self.assertEqual(res, 0)

    def test_perimeter_negative_side(self):
        res = perimeter(-3, 4, 5)
        self.assertEqual(res, 0)

    def test_area_one_values(self):
        res = area(1, 1)
        self.assertEqual(res, 0.5)

    def test_perimeter_one_values(self):
        res = perimeter(1, 1, 1)
        self.assertEqual(res, 3)
