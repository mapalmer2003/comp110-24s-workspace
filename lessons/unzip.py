"""Splitting a dictionary into two lists.""" 

__author__ = "730477567"


def get_keys(input_dict: dict[str, int]) -> list[str]:
    """Takes dict and puts keys in list."""
    list_of_keys: list[str] = []
    for key in input_dict:
        list_of_keys.append(key)
    return list_of_keys


def get_values(input_dict: dict[str, int]) -> list[int]:
    """Takes dict and puts values in list."""
    list_of_keys: list[int] = []
    for key in input_dict:
        list_of_keys.append(input_dict[key])
    return list_of_keys