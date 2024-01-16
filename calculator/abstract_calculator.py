from abc import abstractmethod, ABC
from typing import List, Union

from calculator.validators import AbstractValidator


class AbstractCalculator (ABC):
    validators: List[AbstractValidator] = []

    def run(self, expression: str) -> Union[float, int]:
        """ run the users arithmetic expression

            Parameters
            ----------
            expression : str
                The user's input, e.g.: 1+1
        
            Returns
            -------
            str
                The calculated value, e.g.: 2
        """
        self._validate(expression)
        output = self._calculate(expression)
        return output

    def _validate(self, expression:str) -> None:
        """ validates whether input is a valid arithmetic expression

            Parameters
            ----------
            expression : str
                The user's input, e.g.: 1+1
        
            Raises
            -------
            InvalidInput:
                raises InvalidInput exception when the input is not valid
        """
        if len(self.validators) == 0:
            return

        for validator in self.validators:
            validator.validate(expression)

    @abstractmethod
    def _calculate(self, expression: str) -> Union[float, int]:
        """ calculates an arithmetic expression

            Parameters
            ----------
            expression : str
                The user's input, e.g.: 1+1
        
            Returns
            -------
            str
                The calculated value, e.g.: 2        
        """
