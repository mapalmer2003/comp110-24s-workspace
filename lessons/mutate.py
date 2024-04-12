"""Mutating functions."""

__author__ = "730477576"


def manual_append(a: list[int], b: int) -> None:
    """Takes list of int and adds int into list."""
    a.append(b)


def double(a: list[int]) -> None:
    """Takes list of int and doubles."""
    idx: int = 0
    while idx <= len(a) - 1:
        a[idx] *= 2
        idx += 1