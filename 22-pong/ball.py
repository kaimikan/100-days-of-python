from turtle import Turtle

SPEED = 7.5


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.initialize_ball()
        self.RADIUS = 20
        self.move_speed = SPEED
        self.x_direction = 1
        self.y_direction = 1

    def initialize_ball(self):
        self.shape("circle")
        self.color("orange")
        self.penup()
        self.goto(0, 0)
        self.setheading(45)

    def move(self):
        self.setx(self.xcor() + self.move_speed * self.x_direction)
        self.sety(self.ycor() + self.move_speed * self.y_direction)

    def bounce_y(self):
        if self.ycor() > 0:
            self.y_direction = -1
        else:
            self.y_direction = 1

    def bounce_x(self):
        self.move_speed *= 1.1
        if self.xcor() > 0:
            self.x_direction = -1
        else:
            self.x_direction = 1

    def reset_ball(self):
        self.bounce_x()
        self.move_speed = SPEED
        self.goto(0, 0)
