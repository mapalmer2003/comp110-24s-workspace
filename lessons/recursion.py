"""Writing a recursive function!"""

__author__ = "730477576"


def f(n: int, k: int) -> int:
    """Recursive method for f!"""
    if n == 0:
        return 0
    else:
        return k + f(n - 1, k)
