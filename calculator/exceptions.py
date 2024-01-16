from typing import Optional
from calculator import errors


class UserDefinedException(Exception):
    """ Parent of all user-defined exceptions """
    MESSAGE: Optional[str] = None

    def __init__(self):
        super().__init__(self.MESSAGE)

    def __str__(self) -> str:
        return self.MESSAGE


class DevisionByZeroException(UserDefinedException):
     MESSAGE: Optional[str] =errors.DEVISION_BY_ZERO_ERROR_MSG


class InvalidInputException(UserDefinedException):
     MESSAGE: Optional[str] =errors.INVALID_INPUT_ERROR_MSG


class BigResultException(UserDefinedException):
     MESSAGE: Optional[str] =errors.BIG_RESULT_ERROR_MSG

class EmptyInputException(UserDefinedException):
     MESSAGE: Optional[str] =errors.EMPTY_INPUT_ERROR_MSG


class UnknownErrorException(UserDefinedException):
     MESSAGE: Optional[str] =errors.UNKNOWN_ERROR_MSG
