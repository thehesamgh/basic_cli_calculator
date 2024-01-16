import abc
import re

from calculator.exceptions import EmptyInputException, InvalidInputException

class AbstractValidator:
    @abc.abstractmethod
    def validate(self, string:str) -> None:
        """ run the users arithmetic expression

            Parameters
            ----------
            string : str
                The user's input, e.g.: 1+1
        
            Raises
            ------
            exception if input string is not valid
        """


class RegexValidator(AbstractValidator):
    def __init__(self, pattern: str) -> None:
        self.__pattern = pattern

    def validate(self, string:str) -> None:
        match: re.Match = re.fullmatch(pattern=self.__pattern, string=string)
        is_valid = bool(match)
        if not is_valid:
            raise InvalidInputException

class EmptyInputValidator(AbstractValidator):
    def validate(self, string:str) -> None:
        if string.strip() == "":
            raise EmptyInputException
