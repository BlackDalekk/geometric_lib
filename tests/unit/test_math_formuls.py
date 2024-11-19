import unittest
import math

from tests.unit import circle, rectangle, square, triangle


class TestMathFormuls(unittest.TestCase):
    def test_circle_area(self) -> None:
        res = circle.area(1)
        self.assertEqual(res, math.pi)

    def test_circle_perimeter(self) -> None:
        res = circle.perimeter(1)
        self.assertEqual(res, 2 * math.pi)

    def test_rectangle_get_rectangle_area(self) -> None:
        res = rectangle.get_rectangle_area(1, 2)
        self.assertEqual(res, 2)

    def test_rectangle_get_rectangle_perimeter(self) -> None:
        res = rectangle.get_rectangle_perimeter(1, 2)
        self.assertEqual(res, 6)

    def test_square_area(self) -> None:
        res = square.area(1)
        self.assertEqual(res, 1)

    def test_square_perimeter(self) -> None:
        res = square.perimeter(1)
        self.assertEqual(res, 4)

    def test_triangle_area(self) -> None:
        res = triangle.area(1, 2)
        self.assertEqual(res, 1)

    def test_triangle_perimeter(self) -> None:
        res = triangle.perimeter(1, 2, 3)
        self.assertEqual(res, 6)


if __name__ == "__main__":
    unittest.main()
