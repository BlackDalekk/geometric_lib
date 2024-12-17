from dataclasses import dataclass

import pytest
from _pytest.mark import structures
from contextlib import nullcontext as no_exception

import math

@dataclass
class TestCase:
    data: dict
    test_case_id: str

    def as_param(self) -> tuple:
        return tuple(self.data.values())


def generate_params(test_cases: list[TestCase]) -> tuple:
    return (test_case.as_param() for test_case in test_cases)




_test_circle_area_cases = [
    TestCase(
        data={
            "input_data": 1,
            "expected_data": 3.141592653589793,
            "expected_exception": no_exception(),
        },
        test_case_id="normal",
    ),
    TestCase(
        data={
            "input_data": -1,
            "expected_data": None,
            "expected_exception": pytest.raises(ValueError)
        },
        test_case_id="wrong_input",
    ),
    TestCase(
        data={
            "input_data": 0.123,
            "expected_data": math.pi * 0.015129,
            "expected_exception": no_exception(),
        },
        test_case_id="float_input",
    ),
]

_test_circle_perimeter = [
    TestCase(
        data={
            "input_data": 1,
            "expected_data": 2 * math.pi,
            "expected_exception": no_exception(),
        },
        test_case_id="normal",
    ),
    TestCase(
        data={
            "input_data": 1,
            "expected_data": None,
            "expected_exception": pytest.raises(ValueError),
        },
        test_case_id="wrong_input",
    ),
    TestCase(
        data={
            "input_data": 0.123,
            "expected_data": 0.246 * math.pi,
            "expected_exception": no_exception(),
        },
        test_case_id="float_input_data",
    ),
]

_test_rectangle_get_rectangle_area = [
    TestCase(
        data={
            "input_data": (1, 2),
            "expected_data": 2,
            "expected_exception": no_exception(),
        },
        test_case_id="normal",
    ),
    TestCase(
        data={
            "input_data": (-1, -2),
            "expected_data": None,
            "expected_exception": pytest.raises(ValueError),
        },
        test_case_id="wrong_input",
    ),
    TestCase(
        data={
            "input_data": (0.123, 0.231),
            "expected_data": 0.028413,
            "expected_exception": no_exception(),
        },
        test_case_id="float_input_data",
    ),
]

_test_rectangle_get_rectangle_perimeter = [
    TestCase(
        data={
            "input_data": (1, 2),
            "expected_data": 6,
            "expected_exception": no_exception(),
        },
        test_case_id="normal",
    ),
    TestCase(
        data={
            "input_data": (-1, -2),
            "expected_data": None,
            "expected_exception": pytest.raises(ValueError),
        },
        test_case_id="wrong_input",
    ),
    TestCase(
        data={
            "input_data": (0.123, 0.456),
            "expected_data": 1.158,
            "expected_exception": no_exception(),
        },
        test_case_id="float_input_data",
    ),
]

_test_square_area = [
    TestCase(
        data={
            "input_data": 1,
            "expected_data": 1,
            "expected_exception": no_exception(),
        },
        test_case_id="normal",
    ),
    TestCase(
        data={
            "input_data": -1,
            "expected_data": None,
            "expected_exception": pytest.raises(ValueError),
        },
        test_case_id="wrong_input",
    ),
    TestCase(
        data={
            "input_data": 0.123,
            "expected_data": 0.015129,
            "expected_exception": no_exception(),
        },
        test_case_id="float_input_data",
    ),
]

_test_square_perimeter = [
    TestCase(
        data={
            "input_data": 1,
            "expected_data": 4,
            "expected_exception": no_exception(),
        },
        test_case_id="normal",
    ),
    TestCase(
        data={
            "input_data": -1,
            "expected_data": None,
            "expected_exception": pytest.raises(ValueError),
        },
        test_case_id="wrong_input",
    ),
    TestCase(
        data={
            "input_data": 0.123,
            "expected_data": 0.492,
            "expected_exception": no_exception(),
        },
        test_case_id="float_input_data",
    ),
]

_test_triangle_area = [
    TestCase(
        data={
            "input_data": (1, 2),
            "expected_data": 1,
            "expected_exception": no_exception(),
        },
        test_case_id="normal",
    ),
    TestCase(
        data={
            "input_data": (-1, 2),
            "expected_data": None,
            "expected_exception": pytest.raises(ValueError),
        },
        test_case_id="wrong_input",
    ),
    TestCase(
        data={
            "input_data": (0.1, 0.2),
            "expected_data": 0.1 * 0.2 * 0.5,
            "expected_exception": no_exception(),
        },
        test_case_id="float_input_data",
    ),
]

_test_triangle_perimeter = [
    TestCase(
        data={
            "input_data": (1, 2, 3),
            "expected_data": 6,
            "expected_exception": no_exception(),
        },
        test_case_id="normal",
    ),
    TestCase(
        data={
            "input_data": (-1, 2, -5),
            "expected_data": None,
            "expected_exception": pytest.raises(ValueError),
        },
        test_case_id="wrong_input",
    ),
    TestCase(
        data={
            "input_data": (0.1, 0.2, 0.3),
            "expected_data": 0.1 + 0.2 + 0.3,
            "expected_exception": no_exception(),
        },
        test_case_id="float_input_data",
    ),
]

test_circle_area_cases = generate_params(_test_circle_area_cases)
test_circle_perimeter = generate_params(_test_circle_perimeter)
test_rectangle_get_rectangle_area = generate_params(_test_rectangle_get_rectangle_area)
test_rectangle_get_rectangle_perimeter = generate_params(_test_rectangle_get_rectangle_perimeter)
test_square_area = generate_params(_test_square_area)
test_square_perimeter = generate_params(_test_square_perimeter)
test_triangle_area = generate_params(_test_triangle_area)
test_triangle_perimeter = generate_params(_test_triangle_perimeter)