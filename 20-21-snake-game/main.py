from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.colormode(255)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake(initial_segments=5)
food = Food()
score = Score()

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

    # detect snake and food collision
    if snake.snake_head.distance(food) < snake.SEGMENT_WIDTH:
        food.respawn()
        score.increase_score()
        snake.extend_snake()

    # detect snake and wall collision
    if snake.snake_head.xcor() > SCREEN_WIDTH / 2 - snake.SEGMENT_WIDTH or \
            snake.snake_head.xcor() < (-SCREEN_WIDTH) / 2 + snake.SEGMENT_WIDTH or \
            snake.snake_head.ycor() > SCREEN_HEIGHT / 2 - snake.SEGMENT_WIDTH or \
            snake.snake_head.ycor() < (-SCREEN_HEIGHT) / 2 + snake.SEGMENT_WIDTH:
        game_is_running = False
        score.game_over()

    # detect snake head and other snake segments collision
    # # implementation without slicing
    # for segment in snake.segments:
    #     if segment == snake.snake_head:
    #         pass
    #     elif snake.snake_head.distance(segment) < snake.SEGMENT_WIDTH / 2:
    #         game_is_running = False
    #         score.game_over()
    # implementation with slicing
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < snake.SEGMENT_WIDTH / 2:
            game_is_running = False
            score.game_over()

screen.exitonclick()
