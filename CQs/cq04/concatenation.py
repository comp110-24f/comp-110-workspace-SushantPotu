"""Concatenation file for cq04."""

__author__ = "730768373"

# Initializing variables for the two strings
word1: str = "happy"
word2: str = "tuesday"


def concat(item1: str, item2: str) -> str:
    """Combines the two strings provided and returns them."""
    return item1 + item2


if __name__ == "__main__":
    """Runs the function only if the file is run directly and is not imported."""
    print(concat(word1, word2))
