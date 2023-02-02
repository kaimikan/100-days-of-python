from turtle import Turtle, Screen
import random

has_race_started = False
has_turtle_finished = False
screen = Screen()
screen.setup(width=550, height=500)
bet = screen.textinput(title="Make bet", prompt="Which color of turtle will win the race? "
                                                "(green/orange/blue/purple/red)")
colors = ["green", "orange", "blue", "purple", "red"]
turtle_racers = []

for turtle_number in range(0, len(colors)):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[turtle_number])
    turtle.penup()
    turtle.goto(x=-250, y=125 - 50 * turtle_number)
    turtle_racers.append(turtle)

if bet:
    has_race_started = True

winner_color = ""

while has_race_started and not has_turtle_finished:
    for turtle in turtle_racers:
        if turtle.xcor() > 550 / 2 - 10:
            has_turtle_finished = True
            winner_color = turtle.pencolor()

            if winner_color == bet:
                print(f"You bet on the right turtle! {winner_color} is the winner")
            else:
                print(f"You bet on the {bet} turtle, but {winner_color} was the winner")
        rand_step = random.randint(0, 10)
        turtle.forward(rand_step)

screen.exitonclick()
