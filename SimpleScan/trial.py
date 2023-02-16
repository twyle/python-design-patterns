# -*- coding: utf-8 -*-
"""This script adds and mutiplies two numbers."""

import random


def generate_two_random_numbers(lower: int, upper: int) -> tuple[int]:
    """Gnerate two random numbers between lower and upper.

    Lower and upper must be between 1 and 9 inclusive, and lower must be less
    than upper and both must be integers.

    Args:
        lower (int): The lowest int that can be returned
        upper (int): The largest int that can be returned

    Raises:
        ValueError:
            When lower is greater or equal to upper
            When lower is less than 1 or upper is greater than 9
        TypeError:
            When lower and upper are not integers

    Returns:
        tuple[int]: A tuple with two numbers.
    """

    if not lower or not upper:
        raise ValueError('The inputs must be provided.')
    if not isinstance(lower, int) or not isinstance(upper, int):
        raise TypeError('The lower and upper values must be integers')
    if lower >= upper:
        raise ValueError(
            'The lower value must be smaller than the upper value.')
    if lower < 1 or upper > 9:
        raise ValueError(
            'The lower value cannot be lower than 1 or the upper value cannot be greater than 9.')

    first_number = random.randint(lower, upper)
    second_number = random.randint(lower, upper)

    return (first_number, second_number)
