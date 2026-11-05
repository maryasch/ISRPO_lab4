import unittest
import math
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
       
    def test_circle_area(self):
        res = area(10)
        self.assertEqual(res, 314.1592653589793)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
       
    def test_first_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 62.83185307179586)

    def test_area_type_float(self):
        res = area(5)
        self.assertIsInstance(res, float)

    def test_perimeter_type_float(self):
        res = perimeter(5)
        self.assertIsInstance(res, float)

    def test_area_large_number(self):
        res = area(10**6)
        self.assertAlmostEqual(res, math.pi * 10**12)

    def test_perimeter_large_number(self):
        res = perimeter(10**6)
        self.assertAlmostEqual(res, 2 * math.pi * 10**6)

    def test_area_fractional_radius(self):
        res = area(2.5)
        self.assertAlmostEqual(res, math.pi * 2.5 * 2.5)

    def test_perimeter_fractional_radius(self):
        res = perimeter(2.5)
        self.assertAlmostEqual(res, 2 * math.pi * 2.5)

    def test_area_negative_radius(self):
        res = area(-3)
        self.assertAlmostEqual(res, 0)

    def test_perimeter_negative_radius(self):
        res = perimeter(-3)
        self.assertAlmostEqual(res, 0)

    def test_area_one(self):
        res = area(1)
        self.assertAlmostEqual(res, math.pi)

    def test_perimeter_one(self):
        res = perimeter(1)
        self.assertAlmostEqual(res, 2 * math.pi)
