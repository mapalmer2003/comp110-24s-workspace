"""A bunch of functions that mutate dictionaries."""


__author__ = "730477576"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts a dictionaries keys and values."""
    new_dict: dict[str, str] = {}
    for key in input_dict:
        if input_dict[key] in new_dict:
            raise KeyError("error message of your choice here!")
        new_dict[input_dict[key]] = key
    return new_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    """Takes dictionary of colors and returns favortie."""
    counter: int = 0
    biggest_count: int = 0
    fav_col: str = ""
    for key in input_dict:
        for i in input_dict:
            if input_dict[key] == input_dict[i]:
                counter += 1
        if counter > biggest_count:
            biggest_count = counter
            fav_col = input_dict[key]
        counter = 0 
    return fav_col


def count(provided_list: list[str]) -> dict[str, int]:
    """Takes a list and counts how many times a string is in it."""
    new_dict: dict[str, int] = {}
    counter: int = 1
    for elem in provided_list:
        if elem in new_dict:
            new_dict[elem] += 1
        else:
            new_dict[elem] = counter
    return new_dict


def alphabetizer(provided_list: list[str]) -> dict[str, list[str]]:
    """Takes a list and organizes based on letter strs start with."""
    new_dict: dict[str, list[str]] = {}
    letter_key: str = ""
    for elem in provided_list:
        letter_key = elem.lower()
        letter_key = letter_key[0]
        if letter_key not in new_dict:
            new_dict[letter_key] = []
        new_dict[letter_key].append(elem)
        letter_key = ""
    return new_dict


def update_attendance(given_dict: dict[str, list[str]], day: str, student: str) -> None:
    """Given attendance roster, update it with a new student for a given day."""
    for key in given_dict:
        if key == day:
            if student in given_dict[day]:
                return None
            else:
                given_dict[key].append(student)
    if day not in given_dict:
        given_dict[day] = []
        given_dict[day].append(student)