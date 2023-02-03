from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position, paddle_color):
        super().__init__()
        self.position = position
        self.paddle_color = paddle_color
        self.initiate_paddle()

    def initiate_paddle(self):
        self.shape("square")
        self.color(self.paddle_color)
        # original size is 20x20 we want 20x100
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.position)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 10)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 10)
