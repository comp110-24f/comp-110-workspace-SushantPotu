__author__ = "730768373"

from utils import add_at_index
from utils import only_evens
from utils import sub
import pytest


# only_evens test cases
def test_only_evens_mixed() -> None:
    """Test only_evens with mixed even and odd numbers."""
    test: list[int] = [1, 2, 3, 4]
    assert only_evens(test) == [2, 4]


def test_only_evens_all_odds() -> None:
    """Test only_evens with only odd numbers."""
    test: list[int] = [1, 3, 5]
    only_evens(test)
    assert test == [1, 3, 5]


def test_only_evens_empty_list() -> None:
    """Test only_evens with an empty list."""
    test: list[int] = []
    assert only_evens(test) == []


# sub test cases
def test_sub_normal_case() -> None:
    """Test sub with a normal list and valid indices."""
    test: list[int] = [10, 20, 30, 40]
    assert sub(test, 1, 3) == [20, 30]


def test_sub_out_of_bounds() -> None:
    """Test sub with out-of-bounds indices."""
    test: list[int] = [10, 20, 30]
    assert sub(test, -1, 5) == [10, 20, 30]


def test_sub_empty_list() -> None:
    """Test sub with an empty list."""
    test: list[int] = [1, 3, 5]
    sub(test, 0, 2)
    assert test == [1, 3, 5]


# add_at_index test cases
def test_add_at_index_basic() -> None:
    """Test add_at_index by adding an element to the middle of a list."""
    test: list[int] = [1, 2, 3]
    add_at_index(test, 4, 2)
    assert test == [1, 2, 4, 3]


def test_add_at_index_invalid() -> None:
    """Test add_at_index with an invalid index."""
    test: list[int] = [1, 2, 3]
    with pytest.raises(IndexError):
        add_at_index(test, 4, 5)


def test_add_at_index_mutations() -> None:
    """Test add_at_index for no mutations"""
    test: list[int] = [1, 2, 3]
    result = add_at_index(test, 4, 3)
    assert result == None


test_only_evens_all_odds()
test_only_evens_empty_list()
test_only_evens_mixed()

test_add_at_index_invalid()
test_add_at_index_basic()
test_add_at_index_mutations()

test_sub_empty_list()
test_sub_normal_case()
test_sub_out_of_bounds()
