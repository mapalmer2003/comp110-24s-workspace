"""Tests for the dictionary functions!"""

__author__ = "730477576"

from exercises.ex05.dictionary import invert
from exercises.ex05.dictionary import favorite_color
from exercises.ex05.dictionary import count
from exercises.ex05.dictionary import alphabetizer
from exercises.ex05.dictionary import update_attendance


def test_invert_by_short_dict() -> None:
    """Test wether a short dict is inverted."""
    short_dict: dict[str, str] = {"emotion": "bored"}
    invert(short_dict)
    assert short_dict == {"bored": "emotion"}


def test_invert_by_longer_dict() -> None:
    """Test whether multiple keys invert in a dict."""
    longer_dict: dict[str, str] = {"emotion": "bored", "place": "school"}
    invert(longer_dict)
    assert longer_dict == {"bored": "emotion", "school": "place"}


def test_invert_int_in_dict() -> None:
    """Test whether a int will be accepted in the dict."""
    int_dict: dict[str, str] = {"emotion": "Bored", "age": 10}
    invert(int_dict)
    assert int_dict == TypeError


def test_favorite_color_blue() -> None:
    """Tests to see that the favorite color is blue."""
    blue_fav: dict[str, str] = {"Rachel": "yellow", "Cain": "Blue", "Peter": "Blue"}
    favorite_color(blue_fav)
    assert blue_fav == "blue"


def test_favorite_color_by_alphabetical() -> None:
    """Tests to see that the favorite color is alphabetized."""
    alpha_fav: dict[str, str] = {"Rachel": "yellow", "Cain": "Red", "Peter": "Pink"}
    favorite_color(alpha_fav)
    assert alpha_fav == "pink"


def test_favorite_color_by_non_colors() -> None:
    """Tests to see that function could be for other strings."""
    key_fav: dict[str, str] = {"Yellow": "Rachel", "Red": "Cain", "Pink": "Peter"}
    favorite_color(key_fav)
    assert key_fav == "peter"


def test_count_items_singular() -> None:
    """Tests to see that function counts all items."""
    animal_list: list[str] = ["dog", "cat", "rabit"]
    count(animal_list)
    assert animal_list == {"dog": 1, "cat": 1, "rabit": 1}


def test_count_items_multi() -> None:
    """Tests to see that function counts all items even if multiple."""
    animal_list: list[str] = ["dog", "cat", "dog", "rabit", "dog"]
    count(animal_list)
    assert animal_list == {"dog": 3, "cat": 1, "rabit": 1}


def test_count_items_empty() -> None:
    """Checks to see if dict is intialized given empty list."""
    animal_list: list[str] = []
    count(animal_list)
    assert animal_list == {}


def test_alphabetizer_by_a_b_c() -> None:
    """Tests to see if this function alphabetizes single words."""
    words_to_sort: list[str] = ["apple", "cat", "baseball"]
    alphabetizer(words_to_sort)
    assert words_to_sort == {"a": "apple", "c": "cat", "b": "baseball"}


def test_alphabetizer_multiple() -> None:
    """Tests to see if multiple words are alphabetized correctly."""
    actions_to_sort: list[str] = ["jump", "crouch", "juggle, cram"]
    alphabetizer(actions_to_sort)
    assert actions_to_sort == {"j": ["jump", "juggle"], "c": ["crouch", "cram"]}


def test_alphabetizer_for_blank() -> None:
    """Given blank intalize a dict."""
    nothing_to_sort: list[str] = []
    alphabetizer(nothing_to_sort)
    assert nothing_to_sort == {}


def test_update_attendance_add_new_day() -> None:
    """Tests to see if new day added for student."""
    roll_call: dict[str, list[str]] = {"Monday": ["Jess"], "Wedensday": ["Joe"]}
    name: str = "jane"
    day: str = "Friday"
    update_attendance(roll_call, day, name)
    assert roll_call == {"Monday": ["Jess"], "Wedensday": ["Joe"], "Friday": ["jane"]}


def test_update_attendance_add_same_day() -> None:
    """Tests to see if same day added for student."""
    roll_call: dict[str, list[str]] = {"Monday": ["Jess"], "Wedensday": ["Joe"]}
    name: str = "jane"
    day: str = "Wedensday"
    update_attendance(roll_call, day, name)
    assert roll_call == {"Monday": ["Jess"], "Wedensday": ["Joe", "jane"]}


def test_update_attendance_add_name_as_key() -> None:
    """Tests to see if name can be key."""
    roll_call: dict[str, list[str]] = {"Monday": ["Jess"], "Wedensday": ["Joe"]}
    name: str = "Friday"
    day: str = "Jane"
    update_attendance(roll_call, day, name)
    assert roll_call != {"Monday": ["Jess"], "Wedensday": ["Joe"], "Jane": ["Friday"]}