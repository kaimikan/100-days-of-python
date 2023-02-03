from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from score import Score

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Pong")

# we hide the positioning of the paddle with the tracers
screen.tracer(0)

right_paddle = Paddle((int(SCREEN_WIDTH / 2) - 50, 0), "blue")
left_paddle = Paddle((int(-SCREEN_WIDTH / 2) + 50, 0), "red")
ball = Ball()
score = Score()

game_is_running = True

screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")

while game_is_running:
    screen.update()
    time.sleep(0.05)
    ball.move()

    # detect ball and ceiling/floor collision
    if ball.ycor() > SCREEN_HEIGHT / 2 - ball.RADIUS / 2 or ball.ycor() < (-SCREEN_HEIGHT) / 2 + ball.RADIUS / 2:
        ball.bounce_y()

    # detect ball reaching east or west paddle
    if ball.xcor() > SCREEN_WIDTH / 2 - ball.RADIUS - 50 and ball.distance(right_paddle) < 50 or ball.xcor() < (
            -SCREEN_WIDTH) / 2 + ball.RADIUS + 50 and ball.distance(left_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() > SCREEN_WIDTH / 2:
        ball.reset_ball()
        score.left_point()

    if ball.xcor() < (-SCREEN_WIDTH) / 2:
        ball.reset_ball()
        score.right_point()

screen.exitonclick()
