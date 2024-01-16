import re

from typing import Union
from typing import Final

from calculator.abstract_calculator import AbstractCalculator
from calculator.validators import EmptyInputValidator, RegexValidator

ARITHMETIC_EXPRESSIONS_PATTERN: Final[re.Pattern] = re.compile(r"([0-9]|\+|\(|\)|\-|\*|\/)+")


class BasicCalculator(AbstractCalculator):
    """
    A basic calcuator which uses Pythons interpreter to evaluate user input.
    It checks user's input for any malicious behaviour
    """

    validators = [
        RegexValidator(pattern=ARITHMETIC_EXPRESSIONS_PATTERN),
        EmptyInputValidator(),
    ]

    def _calculate(self, expression: str) -> Union[float, int]:
        return eval(expression)
