"""A house scene with windows, a sky, a door, a frame, clouds, and the sun."""


__author__ = "730477576"


from turtle import Turtle, done
from random import randint


def main() -> None:
    """Lets draw a scene using the lil_guy!"""
    lil_guy: Turtle = Turtle()
    x: float = 0.0 
    y: float = 0.0
    draw_house(lil_guy, x, y)
    draw_roof(lil_guy, x, y)
    draw_sky(lil_guy, x - 100.0, y + 200.0)
    draw_door(lil_guy, x + 22.5, y - 90.0)
    draw_windows(lil_guy, x + 15.0, y - 15.0)
    draw_sun(lil_guy, x + 140.0, y + 170.0)
    draw_cloud(lil_guy, x + 100.0, y + 140.0)
    draw_cloud(lil_guy, x - 10.0, y + 130.0)
    draw_cloud(lil_guy, x + 50.0, y + 130.0)
    draw_cloud(lil_guy, x - 60.0, y + 140.0)
    done()


def draw_house(t: Turtle, x: float, y: float) -> None:
    """Creates house frame."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    what_color: int = randint(1, 3)
    if what_color == 1:
        t.color("Red")
    elif what_color == 2: 
        t.color("Blue")
    else:
        t.color("Brown")
    i: int = 4
    t.begin_fill()
    while i > 0:
        t.forward(90.0)
        t.right(90.0)
        i -= 1
    t.end_fill()
    

def draw_roof(t: Turtle, x: float, y: float) -> None:
    """Draw da roof."""
    t.penup()
    t.setheading(0.0)
    t.goto(x, y)
    t.pendown
    t.color("black")
    t.begin_fill()
    t.left(30.0)
    t.forward(50.0)
    t.setheading(0.0)
    t.right(30.0)
    t.forward(50.0)
    t.end_fill()


def draw_sky(t: Turtle, x: float, y: float) -> None:
    """Creates the sky!"""
    t.penup()
    t.color("skyblue")
    t.setheading(0.0)
    t.goto(x, y)
    t.pendown()
    i: int = 2
    t.begin_fill()
    while i > 0:
        t.forward(300.0)
        t.right(90.0)
        t.forward(90.0)
        t.right(90.0)
        i -= 1
    t.end_fill()


def draw_door(t: Turtle, x: float, y: float) -> None:
    """Draws the door!"""
    t.penup()
    t.color("black")
    t.setheading(0.0)
    t.goto(x, y)
    t.pendown()
    i: int = 2
    t.begin_fill()
    while i > 0:
        t.forward(45.0)
        t.left(90.0)
        t.forward(45.0)
        t.left(90.0)
        i -= 1
    t.end_fill()


def draw_windows(t: Turtle, x: float, y: float) -> None:
    """Now lets do the windows."""
    def recursion(n: int, idx: int) -> None:
        """Recursion loop plus spacing."""
        if n == 0:
            return
        else:
            t.penup()
            t.setheading(0.0)
            t.goto(x + idx, y)
            t.pendown()
            i: int = 4
            t.begin_fill()
            while i > 0:
                t.forward(10.0)
                t.right(90.0)
                i -= 1
            t.end_fill()
            return recursion(n - 1, idx + 30)
    recursion(3, 0)


def draw_sun(t: Turtle, x: float, y: float) -> None:
    """Draw da sun now."""
    t.penup()
    t.color("yellow")
    t.setheading(0.0)
    t.goto(x, y)
    t.pendown()
    i: int = 4
    t.begin_fill()
    while i > 0:
        t.forward(15.0)
        t.right(90.0)
        i -= 1
    t.end_fill()
    

def draw_cloud(t: Turtle, x: float, y: float) -> None:
    """Draw some clouds!"""
    t.penup()
    t.color("white")
    t.setheading(0.0)
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(50, 60)
    t.end_fill()


if __name__ == "__main__":
    main()