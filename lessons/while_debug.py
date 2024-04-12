import turtle

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("white")

    rose = turtle.Turtle()
    rose.shape("turtle")
    rose.color("red")
    rose.speed(10)

    for _ in range(18):
        rose.forward(20)
        rose.right(9)
        rose.forward(20)
        rose.right(27)
        rose.forward(20)
        rose.right(9)
        rose.forward(20)
        rose.right(34)

    rose.hideturtle()
    window.exitonclick()

draw_flower()
