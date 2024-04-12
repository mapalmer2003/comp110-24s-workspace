"""Three ways to sum."""

__author__ = "730477576"


def w_sum(vals: list[float]) -> float:
    """Using while loop to sum."""
    while_index: int = 0
    w_sum: float = 0
    while while_index < len(vals):
        w_sum += vals[while_index]
        while_index += 1
    return w_sum


def f_sum(vals: list[float]) -> float:
    """Using for loop to sum."""
    for_sum: float = 0
    for elem in vals:
        for_sum += elem
    return for_sum


def f_range_sum(vals: list[float]) -> float:
    """Using for_range loop to sum."""
    for_range_sum: float = 0
    for elem in range(0, len(vals)):
        for_range_sum += vals[elem]
    return for_range_sum