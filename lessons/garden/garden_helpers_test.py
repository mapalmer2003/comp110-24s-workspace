"""Test my garden functions."""

__author__ = "730477576"

from lessons.garden.garden_helpers import add_by_date
from lessons.garden.garden_helpers import add_by_kind
from lessons.garden.garden_helpers import lookup_by_kind_and_date


def test_add_by_kind_onion() -> None:
    """Test wether onion is added or not."""
    harvest: dict[str, list[str]] = {"veggie": ["carrot", "lettuce"], "flower": ["rose"]}
    name: str = "onion"
    type: str = "veggie"
    add_by_kind(harvest, type, name) 
    assert harvest == {"veggie": ["carrot", "lettuce", "onion"], "flower": ["rose"]}


def test_add_by_kind_blank() -> None:
    """Test what happens if flower is added to blank dict."""
    given_dict: dict[str, list[str]] = {}
    key_str: str = "flower"
    value_str: str = "sunflower"
    add_by_kind(given_dict, key_str, value_str)
    assert given_dict == {"flower": ["sunflower"]}


def test_add_by_date_rose() -> None:
    """Test what happens if a rose is added in august."""
    given_dict: dict[str, list[str]] = {"January": ["tulip"], "August": ["raddish"]}
    key_str: str = "August"
    value_str: str = "sunflower"
    add_by_date(given_dict, key_str, value_str)
    assert given_dict == {"January": ["tulip"], "August": ["raddish", "sunflower"]}


def test_add_by_date_blank() -> None:
    """Test what happens if a rose is added in august in a blank dict."""
    given_dict: dict[str, list[str]] = {}
    key_str: str = "August"
    value_str: str = "sunflower"
    add_by_date(given_dict, key_str, value_str)
    assert given_dict == {"August": ["sunflower"]}


def test_lookup_by_kind_and_date_for_flower_and_june() -> None:
    """Checks for flowers in august and prints."""
    name_str: dict[str, list[str]] = {"flowers": ["rose", "lily"], "fruits": ["apple", "grape"]}
    dates_str: dict[str, list[str]] = {"August": ["rose", "grape"], "October": ["lily", "apple"]}
    type: str = "flowers"
    date: str = "August"
    assert lookup_by_kind_and_date(name_str, dates_str, type, date) == "flowers to plant in August: rose"


def test_lookup_by_kind_and_date_for_int() -> None:
    """Checks to make sure ints are not accepted."""
    name_str: dict[str, list[str]] = {"flowers": ["rose", "lily"], "fruits": ["apple", "grape"]}
    dates_str: dict[str, list[str]] = {"August": ["rose", "grape"], "October": ["lily", "apple"]}
    type: str = "flowers"
    date: int = 12
    assert lookup_by_kind_and_date(name_str, dates_str, type, date) != "No flowers to plant in 12"
