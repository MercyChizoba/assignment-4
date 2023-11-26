"""Write a Python function that takes two integer inputs from the user and 
calculates their division. Handle the ZeroDivisionError and prompt the user 
to re-enter the secondnumber if it is zero."""


def someint():
    try:
        firstnumb = int(input("Enter a number "))
        secondnumb = int(input("Enter a number "))
        result = firstnumb / secondnumb
        print(f"{firstnumb} / {secondnumb} = {result}")
    except ZeroDivisionError as e:
        print("0 is not a valid number, Please enter a valid number ")
        someint()


someint()

"""Use a custom exception called InvalidInputError to handle cases where the user
inputs non-integer values.
- Test your function with different inputs, including valid and invalid 
values, and ensure thatthe exceptions are raised and handled correctly."""


class InvalidInputError(Exception):
    pass


def someint():
    firstnumb = int(input("Enter a number "))
    secondnumb = int(input("Enter a number "))
    result = firstnumb / secondnumb
    print(f"{firstnumb} / {secondnumb} = {result}")
    if firstnumb or secondnumb != int:
        raise InvalidInputError("not a valid number")
    else:
        pass


try:
    someint()
except InvalidInputError as ex:
    print("Wrong value ")
except Exception as ex:
    print("something else happened")

# THE EXCEPTIONS DIDNT WORK. I TRIED DIFFERENT VALUES AND THE ERRORS WERENT HANDLED

"""Pytest:
- Write a simple Python function that takes two numbers as inputs and returns 
their sum. Write a pytest function to test this function and verify that it 
returns the correct sum for different input values."""

import pytest
import test

# def takeinput(a, b):
# return a + b


def test_takeinput():
    result = takeinput(4, 5)
    assert result == 9
