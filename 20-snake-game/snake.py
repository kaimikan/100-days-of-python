from turtle import Turtle
import random

NORTH = 90
WEST = 0
EAST = 180
SOUTH = 270


class Snake:
    def __init__(self, initial_segments):
        self.SEGMENT_WIDTH = 20
        self.segments = []

        # we throw an error if the segment amount is not ok or just overwrite it to 3
        if not (isinstance(initial_segments, (int, float)) and initial_segments > 0):
            initial_segments = 3
            # raise ValueError(f"positive segment amount expected, got {initial_segments}")

        self.init_snake(initial_segments=initial_segments)
        self.snake_head = self.segments[0]

    def init_snake(self, initial_segments):
        snake_segments = []
        for i in range(0, initial_segments):
            snake_segment = Turtle(shape="square")
            random_green = random.randint(100, 255)
            snake_segment.color(50, random_green, 50)
            snake_segment.penup()
            snake_segment.setx(-self.SEGMENT_WIDTH * i)
            snake_segments.append(snake_segment)

        self.segments = snake_segments

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):  # (start= 2, stop=0, step=-1):
            previous_segment_x = self.segments[segment - 1].xcor()
            previous_segment_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(previous_segment_x, previous_segment_y)

            # because of the loop above we only need to move the first segment and the rest follow it
        self.segments[0].forward(self.SEGMENT_WIDTH)

    # we only need to change the heading of the first segment, it auto moves forward and the rest auto follow it
    def up(self):
        # it should not be possible to go back on itself
        if self.snake_head.heading() != SOUTH:
            self.snake_head.setheading(NORTH)

    def down(self):
        if self.snake_head.heading() != NORTH:
            self.snake_head.setheading(SOUTH)

    def left(self):
        if self.snake_head.heading() != WEST:
            self.snake_head.setheading(EAST)

    def right(self):
        if self.snake_head.heading() != EAST:
            self.snake_head.setheading(WEST)
