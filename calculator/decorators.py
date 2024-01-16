from typing import Callable

from calculator import exceptions

def print_error_message_on_exception(func: Callable):
    """ A decorator which print exception message if any happens """

    def wrapper(*args, **kwrgs):
        try:
            return func(*args, **kwrgs)
        except Exception as exp:
            print(exp, "\n")
            return None
    return wrapper

def convert_exceptions(func: Callable):
    """ A decorator which converts python built-in exceptions to the user-defined exceptions """

    exceptions_mapping: dict = {
        ZeroDivisionError: exceptions.DevisionByZeroException,
        SyntaxError: exceptions.InvalidInputException,
        ValueError: exceptions.InvalidInputException,
        Exception: exceptions.UnknownErrorException,
    }
    def wrapper(*args, **kwrgs):
        try:
            return func(*args, **kwrgs)
        except exceptions.UserDefinedException as exp:
            raise exp
        except Exception as exp:
            raise exceptions_mapping.get(exp, exceptions_mapping[Exception])

    return wrapper
