"""Functions that implement sorting algorithms."""

__author__ = "730477576"


def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.Insert into an already sorted list."""
    sort_ctr: int = 0 
    while sort_ctr < len(x) - 1:
        unsort_idx: int = sort_ctr + 1
        current_element: int = x[unsort_idx]
        while unsort_idx > 0 and x[unsort_idx - 1] > current_element:
            swap_val: int = x[unsort_idx]
            x[unsort_idx] = x[unsort_idx - 1]
            x[unsort_idx - 1] = swap_val
            unsort_idx -= 1
            swap_val = 0
        sort_ctr += 1
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. Repeatedly find the minimum and swap it."""
    ctr: int = 0
    while ctr < len(x):
        idx: int = 0
        while idx < len(x):
            value_store: int = 0
            if x[idx] > x[ctr]:
                value_store = x[idx]
                x[idx] = x[ctr]
                x[ctr] = value_store
            idx += 1
        ctr += 1
    return None
