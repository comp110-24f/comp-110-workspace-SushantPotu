__author__ = "730768373"


def only_evens(vals: list[int]) -> list[int]:
    """Returns a list of all the even numbers in the original list."""
    result: list[int] = []
    # For loop to check each value
    for i in vals:
        if (i % 2) == 0:
            result.append(i)
    return result


def sub(vals: list[int], start: int, stop: int) -> list[int]:
    """Returns a sub list of the original list."""
    # if statements to check for different conditions such as the start/stop indexes and length of original list
    if start < 0:
        start = 0
    if stop > len(vals):
        stop = len(vals)
    if start >= len(vals) or stop <= 0 or len(vals) == 0:
        return []
    return vals[start:stop]


def add_at_index(vals: list[int], value: int, index: int) -> None:
    """Adds a value at a given index in the list."""
    # Check if index is out of range.
    if index < 0 or index > len(vals):
        raise IndexError("Index is out of bounds for the input list")
    else:
        # Moving over each value to the right by one index and putting the value at the chosen index
        vals.append(0)
        for i in range(len(vals) - 1, index, -1):
            vals[i] = vals[i - 1]
        vals[index] = value
    return None
