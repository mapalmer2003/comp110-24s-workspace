"""Comapring methods that mutate and do not."""

from __future__ import annotations

__author__ = "730477576"


class Point:
    """Makes a point."""
    x: float
    y: float


    def __init__(self, x_input: float, y_input: float):
        """Add ability to input val."""
        self.x = x_input
        self.y = y_input
    

    def scale_by(self, factor: int) -> None:
        """Scales the point."""
        self.x *= factor
        self.y *= factor

    
    def scale(self, factor: int) -> Point:
        """Creates new point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point