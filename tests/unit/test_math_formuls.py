import unittest
from typing import Callable, TypeVar
from _pytest.python_api import RaisesContext
from parameterized import parameterized
from contextlib import nullcontext as no_exception

from tests.unit import circle, rectangle, square, triangle
from . import cases

T = TypeVar("T")


class TestMathFormuls(unittest.TestCase):
    @parameterized.expand((cases.test_circle_area_cases))
    def test_circle_area(
        self,
        input_data: int | float,
        expected_data: int | float,
        expected_exception: RaisesContext,
    ) -> None:
        self._check(
            circle.area,
            (input_data,),
            expected_data,
            expected_exception,
        )

    @parameterized.expand((cases.test_circle_perimeter))
    def test_circle_perimeter(
        self,
        input_data: int | float,
        expected_data: int | float,
        expected_exception: RaisesContext,
    ) -> None:
        self._check(
            circle.perimeter,
            (input_data,),
            expected_data,
            expected_exception,
        )

    @parameterized.expand((cases.test_rectangle_get_rectangle_area))
    def test_rectangle_get_rectangle_area(
        self,
        input_data: tuple[int | float, int | float],
        expected_data: int | float,
        expected_exception: RaisesContext,
    ) -> None:
        self._check(
            rectangle.get_rectangle_area,
            input_data,
            expected_data,
            expected_exception,
        )

    @parameterized.expand((cases.test_rectangle_get_rectangle_perimeter))
    def test_rectangle_get_rectangle_perimeter(
        self,
        input_data: tuple[int | float, int | float],
        expected_data: int | float,
        expected_exception: RaisesContext,
    ) -> None:
        self._check(
            rectangle.get_rectangle_perimeter,
            input_data,
            expected_data,
            expected_exception,
        )

    @parameterized.expand((cases.test_square_area))
    def test_square_area(
        self,
        input_data: int | float,
        expected_data: int | float,
        expected_exception: RaisesContext,
    ) -> None:
        self._check(
            square.area,
            (input_data, ),
            expected_data,
            expected_exception,
        )

    @parameterized.expand((cases.test_square_perimeter))
    def test_square_perimeter(
        self,
        input_data: int | float,
        expected_data: int | float,
        expected_exception: RaisesContext,
    ) -> None:
        self._check(
            square.perimeter,
            (input_data, ),
            expected_data,
            expected_exception,
        )

    @parameterized.expand((cases.test_triangle_area))
    def test_triangle_area(
        self,
        input_data: tuple[int | float, int | float],
        expected_data: int | float,
        expected_exception: RaisesContext,
    ) -> None:
        self._check(
            triangle.area,
            input_data,
            expected_data,
            expected_exception,
        )

    @parameterized.expand((cases.test_triangle_perimeter))
    def test_triangle_perimeter(
        self,
        input_data: tuple[int | float, int | float, int | float],
        expected_data: int | float,
        expected_exception: RaisesContext,
    ) -> None:
        self._check(
            triangle.perimeter,
            input_data,
            expected_data,
            expected_exception,
        )

    def _check(
        self,
        function: Callable,
        args: tuple,
        expected_result: T,
        expected_exception: RaisesContext,
    ) -> None:
        with expected_exception:
            result = function(*args)
            self.assertEqual(result, expected_result)
