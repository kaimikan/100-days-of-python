from turtle import Turtle, Screen

franklin = Turtle()
screen = Screen()


def forwards():
    franklin.forward(10)


def backwards():
    franklin.forward(-10)


def clockwise():
    franklin.right(10)


def counter_clockwise():
    franklin.left(10)


def reset():
    franklin.clear()
    franklin.penup()
    franklin.home()
    franklin.pendown()


screen.listen()
screen.onkeypress(key="w", fun=forwards)
screen.onkeypress(key="s", fun=backwards)
screen.onkeypress(key="d", fun=clockwise)
screen.onkeypress(key="a", fun=counter_clockwise)
screen.onkeypress(key="c", fun=reset)
screen.exitonclick()
