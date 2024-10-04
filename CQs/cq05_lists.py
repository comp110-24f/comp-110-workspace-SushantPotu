"""Mutating functions."""

__author__ = "730768373"


def manual_append(a: list[int], b: int) -> None:
    """Appends given int onto list."""
    a.append(b)


# Test cases.
a: list[int] = [1, 2, 3]
manual_append(a, 2)
print(a)


def double(inputList: list[int]) -> None:
    """Doubles each of the values in the input list."""
    i: int = 0
    while i < len(inputList):
        inputList[i] *= 2
        i += 1


# Test cases.
list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)
