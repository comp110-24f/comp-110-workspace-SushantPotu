__author__ = "730768373"


def all(inputList: list[int], inputNum: int) -> bool:
    """Function that checks all elements of a list to see if it matches the given int."""
    # Checks if the length is zero and returns False.
    if len(inputList) == 0:
        return False
    # Checks if there is any value in the list that doesn't match the input number and returns false if one is found.
    # Returns early if one is found, otherwise returns at end.
    for item in inputList:
        if item != inputNum:
            return False
    return True


def max(inputList: list[int]) -> int:
    """Function that checks for the max value in a list."""
    # Checks if the length is zero and raises error.
    if len(inputList) == 0:
        raise ValueError("max() arg is an empty List")
    # Takes the first item in the list and compares each of the numbers in the list to it,
    # changing the max num variable value to whichever number is found and repeats until list ends.
    max_num = inputList[0]
    for num in inputList:
        if num > max_num:
            max_num = num
    return max_num


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Function to check if the two lists are equal"""
    # Checks if lengths of both lists are equal
    if len(list1) != len(list2):
        return False
    # Compares each element of both lists and returns true/false.
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    """Function that extends the first list using values from the second list and appending them."""
    # Loops through each element of second list and appends it to the first list.
    for item in list2:
        list1.append(item)


# Test cases
print(all([1, 2, 3], 1))
print(all([1, 1, 1], 2))
print(all([1, 1, 1], 1))


print(max([100, 99, 98]))

a: list[int] = [1, 3, 5]
b: list[int] = [2, 4, 6]
extend(a, b)
print(a)
