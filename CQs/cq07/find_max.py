__author__ = "730768373"


def find_and_remove_max(vals: list[int]) -> int:
    """Finds max value, returns it, and removes all instances of it from list"""
    # Checks if list is empty
    if vals == []:
        return -1
    # If list is not empty runs the following.
    # Checks for max value in list.
    max: int = vals[0]
    for num in vals:
        if num > max:
            max = num
    # Loop through to remove max values.
    i: int = 0
    while i < len(vals):
        if vals[i] == max:
            vals.pop(i)
        else:
            i += 1
    # Returning the max value.
    return max


# Test cases
b: list[int] = [10, 10, 9, 8, 7, 10]
print(find_and_remove_max(b))
print(b)
