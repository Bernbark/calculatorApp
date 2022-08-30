"""Calculator Functions

This script contains methods which are typically found on a calculator.

This script requires no imports or installs yet.

This file can also be imported as a module and contains the following
functions:

    * add - returns the sum of two numbers
    * subtract - the main function of the script


"""


def add(a, b):
    """Returns the sum of a and b

    :param a: number to be added to b
    :param b: number to be added to a
    :return: the sum of a and b
    """
    return a + b


def subtract(a, b):
    """Returns the difference between a and b (order matters)

    :param a: number to be subtracted from b
    :param b: number to be subtracted from a
    :return: a - b
    """
    return a - b


def divide(a, b):
    """Returns the result of a divided by b

    :param a: number to be subtracted from b
    :param b: number to be subtracted from a
    :return: a / b
    """
    if b == 0:
        return "Undefined"
    return a / b