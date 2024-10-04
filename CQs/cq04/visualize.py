"""Visualize file for cq04."""

__author__ = "730768373"

from CQs.cq04.concatenation import concat
from CQs.cq04.coordinates import get_coords

# initialized the two variables x and y
x: str = "123"
y: str = "abc"

# Calling the functions, each imported from the concatenation file and coordinates files.
print(concat(x, y))
get_coords(x, y)
