__author__ = "730768373"

from find_max import find_and_remove_max


def test_find_and_remove_max() -> None:
    """Function to run all test cases for the find_and_remove() function."""

    # Test 1: checks if it correctly returns the max value
    test: list[int] = [2, 5, 9, 6]
    assert find_and_remove_max(test) == 9
    print("Test 1 passed!")

    # Test 2: checks if it correctly removes all instances of the max value
    test = [7, 5, 7, 1]
    find_and_remove_max(test)
    assert test == [5, 1]
    print("Test 2 passed!")

    # Test 3: checks if it correctly removes all of the max values and returns correct max value given a list full of the same number
    test = [8, 8, 8, 8, 8]
    assert find_and_remove_max(test) == 8
    assert test == []
    print("Test 3 passed!")

    print("All tests passed!")


test_find_and_remove_max()
