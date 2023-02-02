import random
from turtle import Turtle, Screen

# avoid using * -> from turtle import *
# much better readability without it

# alias importing -> import random as rand
import random as rand

# to get color scheme of damien hirst painting
import colorgram

# Turtle graphics docs: https://docs.python.org/3/library/turtle.html
franklin = Turtle()
franklin.shape("turtle")
franklin.color("DarkGreen")
screen = Screen()
# this is for the increasing angles task (there are easier ways to do it though like just random.random())
screen.colormode(255)


def hirst_painting():
    painting_colors = colorgram.extract('damien_hirst.jpg', 25)
    rgb_dots = []
    for color in painting_colors:
        rgb_dots.append((color.rgb.r, color.rgb.g, color.rgb.b))

    rows = 5
    dots_per_row = int(len(rgb_dots) / rows)
    color_index = 0
    franklin.speed("fastest")
    franklin.hideturtle()
    for row in range(0, rows):
        for dot in range(0, dots_per_row):
            franklin.color(rgb_dots[color_index])
            color_index += 1
            franklin.dot(25)
            franklin.penup()
            franklin.forward(50)
            franklin.pendown()

        franklin.penup()
        franklin.setheading(90)
        franklin.forward(50)
        franklin.setheading(180)
        franklin.forward(50 * rows)
        franklin.setheading(0)
        franklin.pendown()

    pass


def circle_of_circles():
    circle_amount = 20
    franklin.speed("fastest")
    for i in range(0, circle_amount):
        rgb_tuple = (rand.randint(0, 255), rand.randint(0, 255), rand.randint(0, 255))
        franklin.color(rgb_tuple)
        franklin.circle(50)
        franklin.setheading(franklin.heading() + 360 / circle_amount)


def random_walk():
    # RANDOM WALK
    cycles = 365
    while cycles:
        random_number = rand.randint(0, 100)
        rgb_tuple = (rand.randint(0, 255), rand.randint(0, 255), rand.randint(0, 255))
        franklin.color(rgb_tuple)
        if random_number <= 25:
            franklin.left(90)
        elif random_number <= 50:
            franklin.left(180)
        elif random_number <= 75:
            franklin.left(270)
        # else we don't rotate

        # # we can replace it with
        # compass = [0, 90, 270, 360]
        # franklin.setheading(random.choice(compass))
        franklin.pensize(10)
        franklin.forward(25)
        franklin.speed("fastest")
        cycles += 1


def from_triangle_to_octagon():
    # # INCREASING ANGLES - from triangle to octagon
    for i in range(0, 8):
        franklin.color(rand.randint(0, 255), rand.randint(0, 255), rand.randint(0, 255))
        print(f"i: {i}")
        for y in range(0, 3 + i):
            print(f"y: {y}")
            franklin.right(360 / (3 + i))
            franklin.forward(50)


def dotted_line():
    # # DOTTED LINE
    for i in range(0, 50):
        franklin.pendown()
        franklin.forward(1)
        franklin.penup()
        franklin.forward(1)


def square():
    # # SQUARE
    for i in range(0, 4):
        franklin.forward(50)
        franklin.right(90)


def menu():
    try_again = True
    while try_again:
        menu_options = "0. hirst painting()\n" \
                       "1. circle_of_circles()\n" \
                       "2. random_walk()\n" \
                       "3. from_triangle_to_octagon()\n" \
                       "4. dotted_line()\n" \
                       "5. square()"
        print(menu_options)
        methods = [hirst_painting, circle_of_circles, random_walk, from_triangle_to_octagon, dotted_line,
                   square]
        choice = int(input("Select a number from 0 to 5: "))
        while choice < 0 or choice > 5:
            choice = int(input("Select a number from 0 to 5: "))

        print("the turtle is drawing...")
        methods[choice]()
        do_it_again = input("Go again 'y' or 'n': ")
        while do_it_again != 'y' and do_it_again != 'n':
            do_it_again = input("Go again 'y' or 'n': ")
        if do_it_again == 'n':
            try_again = False


menu()

# # tuple and array difference -> we cannot change a tuple once it has been created
# my_rgb_tuple = (72, 72, 7)
# print(my_rgb_tuple[0])
# my_rgb_list = [72, 72, 7]
# my_rgb_list[2] = 72

# this code stays at the bottom
screen.exitonclick()
