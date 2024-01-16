from typing import Union

from calculator.basic_calculator import BasicCalculator
from calculator.decorators import convert_exceptions, print_error_message_on_exception

@convert_exceptions
def run_calculation(expression: str) -> Union[int, float]:
    result = BasicCalculator().run(expression)
    return result

@convert_exceptions
def print_output(result, *args, **kwrgs):
    print(result, *args, **kwrgs)

@print_error_message_on_exception
def main():
    users_expression: str = input("please enter en arithmetic expression:\n >")
    result = run_calculation(users_expression)
    print_output(result, "\n")


if __name__ == "__main__":
    while True:
        main()
