"""Coordinates file for cq04."""

__author__ = "730768373"


def get_coords(xs: str, ys: str) -> None:
    """Makes the formatted version of the two strings"""
    i: int = 0
    y: int = 0

    # Iterates over all characters in second string and adds to each of the characters in first string.
    while i < len(xs):
        y = 0
        while y < len(ys):
            print(xs[i], ys[y])
            y += 1
        i += 1


# Test cases
get_coords("12", "34")
get_coords("hi", "bye")
