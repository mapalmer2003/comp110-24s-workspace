"""List utility functions."""

__author__ = "730477576"


def all(given_list: list[int], compare_val: int) -> bool:
    """Are all of a list equal to a value."""
    if len(given_list) == 0:
        return False
    idx: int = 0
    while idx < len(given_list):
        if given_list[idx] == compare_val:
            idx += 1
        else:
            return False
    return True


def max(given_list: list[int]) -> int:
    """Obtains max of list."""
    if len(given_list) == 0:
        raise ValueError("max() arg is an empty List")
    idx: int = 1
    max: int = given_list[0]
    while idx < len(given_list):
        if max < given_list[idx]:
            max = given_list[idx]
        idx += 1
    return max


def is_equal(given_list: list[int], another_list: list[int]) -> bool:
    """Check if two lists have equal values."""
    if len(given_list) != len(another_list):
        return False
    idx: int = 0
    while idx < len(given_list) and idx < len(another_list):
        if given_list[idx] == another_list[idx]:
            idx += 1
        else:
            return False
    return True


def extend(given_list: list[int], another_list: list[int]) -> None:
    """Extends a list with values of another list."""
    idx: int = 0 
    while idx < len(another_list):
        given_list.append(another_list[idx])
        idx += 1
