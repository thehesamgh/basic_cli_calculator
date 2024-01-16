import pytest

from calculator.basic_calculator import BasicCalculator
from calculator.exceptions import InvalidInputException


@pytest.mark.parametrize("input, exception", [
    ('lamda:print("123")', InvalidInputException),
    ('1**********2', SyntaxError),
    ('1*/2', SyntaxError),
    ('4///2', SyntaxError),
    ('4*/2', SyntaxError),
    ('4*(2', SyntaxError),
])
def test_raise_exception_on_non_arithmetic_expressions(input, exception):
    with pytest.raises(exception):
        BasicCalculator().run(input)

@pytest.mark.parametrize("input, expected_output", [
    ('1+-+1', 0),
    ('1+++1', 2),
    ('1/+2', 0.5),
])
def test_run_method(input, expected_output):
    actual_output =  BasicCalculator().run(input)
    assert expected_output == actual_output
