# -*- coding: utf-8 -*-
"""This script adds and mutiplies two numbers."""

import pytest
from ..trial import generate_two_random_numbers


def test_trial_generate_two_numbers():
    """Assert that two integers are generated."""
    numbers = generate_two_random_numbers(2, 7)
    assert isinstance(numbers, tuple)
    assert isinstance(numbers[0], int)
    assert isinstance(numbers[1], int)


def test_raises_valuerror():
    """When given None as input, raises ValueError."""
    with pytest.raises(ValueError):
        generate_two_random_numbers(None, 1)


def test_raises_typerror():
    """When given non-integer values."""
    with pytest.raises(TypeError):
        generate_two_random_numbers(3.5, 1.2)


def test_raises_valuerror_lower_greater():
    """When lower is greater than upper."""
    with pytest.raises(ValueError):
        generate_two_random_numbers(5, 3)
