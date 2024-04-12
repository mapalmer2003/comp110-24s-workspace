"""Some functions for my garden plan!""" 

__author__ = "730477576"


def add_by_kind(given_dict: dict[str, list[str]], key_var: str, value_var: str) -> None:
    """Takes str and adds to given dict at a given key."""
    if key_var in given_dict:
        given_dict[key_var].append(value_var)
    else:
        given_dict[key_var] = []
        given_dict[key_var].append(value_var)


def add_by_date(given_dict: dict[str, list[str]], key_str: str, value_str: str) -> None:
    """Takes list an adds flower by date to be sown."""
    if key_str in given_dict:
        given_dict[key_str].append(value_str)
    else:
        given_dict[key_str] = []
        given_dict[key_str].append(value_str)


def lookup_by_kind_and_date(name_str: dict[str, list[str]], dates_str: dict[str, list[str]], type: str, date: str) -> str:
    """Takes date and name string and prints out specific plants from that date."""
    assert type in name_str
    assert date in dates_str
    new_list: list[str] = []
    for plant in name_str[type]:
        for other_plant in dates_str:
            if plant == other_plant:
                new_list.append(other_plant)
    if new_list == []:
        return (f"No {type} to plant in {date}.")
    else:
        return (f"{type} to plant in {date}: {new_list}")