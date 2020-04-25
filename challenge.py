import math


def square_area(side):
    return round(side * side, 2)


def rectangle_area(base, height):
    return round(base * height, 2)


def triangle_area(base, height):
    return round(base * height / 2, 2)


def rhombus_area(diagonal_1, diagonal_2):
    return round(diagonal_1 * diagonal_2 / 2, 2)


def trapezoid_area(base_minor, base_major, height):
    return round(((base_minor + base_major) * height) / 2, 2)


def regular_polygon_area(perimeter, apothem):
    return round(perimeter * apothem / 2, 2)


def circumference_area(radius):
    return round(math.pi * pow(radius, 2), 2)


if __name__ == '__main__':
    import unittest

    class GeometrySuite(unittest.TestCase):

        def setUp(self):
            self.values = {
                'side': 4.0,
                'base': 2.0,
                'height': 3.0,
                'diagonal_1': 5.0,
                'diagonal_2': 8.0,
                'base_minor': 5.0,
                'base_major': 3.0,
                'perimeter': 36.0,
                'apothem': 4.0,
                'radius': 3.0
            }

        def test_square_area(self):
            self.assertEqual(16.0, square_area(self.values['side']))

        def test_rectangle_area(self):
            self.assertEqual(6.0, rectangle_area(self.values['base'], self.values['height']))

        def test_triangle_area(self):
            self.assertEqual(3.0, triangle_area(self.values['base'], self.values['height']))

        def test_rhombus_area(self):
            self.assertEqual(20.0, rhombus_area(self.values['diagonal_1'], self.values['diagonal_2']))

        def test_trapezoid_area(self):
            self.assertEqual(12.0, trapezoid_area(self.values['base_minor'], self.values['base_major'], self.values['height']))

        def test_regular_polygon_area(self):
            self.assertEqual(72.0, regular_polygon_area(self.values['perimeter'], self.values['apothem']))

        def test_circumference_area(self):
            self.assertEqual(28.27, circumference_area(self.values['radius']))

        def tearDown(self):
            del(self.values)

    unittest.main()
