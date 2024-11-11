"""Summing the elements of a list using different loops"""

__author__ = "730768373"


def w_sum(vals: list[float]) -> float:
    """Uses a while loop to iterate through values and sums each of them together."""
    # intializing variables
    sum: float = 0.0
    i: int = 0
    # while loop for iteration
    while i < len(vals):
        sum += vals[i]
        i += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Uses the built-in sum function to add together each value of i for each item in vals"""
    return sum(i for i in vals)


def f_range_sum(vals: list[float]) -> float:
    """Uses the built-in sum function to add together each value of i for each item in vals using a in range for loop and indexing each item in list"""
    return sum(vals[i] for i in range(len(vals)))


# Test Cases
print(w_sum([1.1, 0.9, 1.0]))
print(f_sum([1.1, 0.9, 1.0]))
print(f_range_sum([1.1, 0.9, 1.0]))
