from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.colormode(255)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake(initial_segments=5)

# listen for key presses and call equivalent methods in the snake class
screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_is_running = True
while game_is_running:
    # works together with screen.trace()
    # we use it to make it seem like the segments are moving at the same time
    screen.update()

    time.sleep(0.1)

    snake.move()

screen.exitonclick()
