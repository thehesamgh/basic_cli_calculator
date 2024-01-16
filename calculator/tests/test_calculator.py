import pytest

from calculator.basic_calculator import BasicCalculator
from calculator.exceptions import InvalidInputException


@pytest.mark.parametrize("input_expression, exception", [
    ('lamda:print("123")', InvalidInputException),
    ('1**********2', SyntaxError),
    ('1*/2', SyntaxError),
    ('4///2', SyntaxError),
    ('4*/2', SyntaxError),
    ('4*(2', SyntaxError),
])
def test_raise_exception_on_non_arithmetic_expressions(input_expression, exception):
    with pytest.raises(exception):
        BasicCalculator().run(input_expression)

@pytest.mark.parametrize("input_expression, expected_output", [
    ('1+-+1', 0),
    ('1+++1', 2),
    ('1/+2', 0.5),
])
def test_run_method(input_expression, expected_output):
    actual_output =  BasicCalculator().run(input_expression)
    assert expected_output == actual_output
