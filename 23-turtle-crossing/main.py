from turtle import Screen
import time
from crosser import Crosser
from car_control import CarControl
from score import Score

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
# tracer to hide the initial movement of the positioning 'turtles'
screen.tracer(0)
screen.bgcolor("#777777")
screen.title("Turtle Crossing")
# so we can have random color cars
screen.colormode(255)

crosser = Crosser(SCREEN_WIDTH, SCREEN_HEIGHT)
car_control = CarControl(number_of_cars=5, screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT)
score = Score(SCREEN_WIDTH, SCREEN_HEIGHT)

game_is_running = True

screen.listen()
screen.onkeypress(crosser.cross, "Up")

while game_is_running:
    # simulate a fluent movement
    time.sleep(0.1)
    screen.update()
    car_control.move_cars()

    # detect crosser reaching top line
    if crosser.is_crosser_at_finish_line():
        crosser.back_to_start()
        score.next_level()
        car_control.increase_cars_speed()

    # detect crosser and car collision
    for car in car_control.cars:
        # DAMN PYTHON IS CRAZY!
        # turn this
        # # if crosser.xcor() < car.xcor() + car.CAR_WIDTH / 2 and crosser.xcor() > car.xcor() - car.CAR_WIDTH / 2:
        # into this
        # # if car.xcor() + car.CAR_WIDTH / 2 > crosser.xcor() > car.xcor() - car.CAR_WIDTH / 2:
        if car.xcor() + car.CAR_WIDTH / 2 > crosser.xcor() > car.xcor() - car.CAR_WIDTH / 2 and \
                car.ycor() + car.CAR_HEIGHT / 2 + crosser.CROSSER_SIZE / 2 > crosser.ycor() > car.ycor() - \
                car.CAR_HEIGHT / 2 - crosser.CROSSER_SIZE / 2:
            crosser.back_to_start()
            crosser.reincarnate()
            score.reset_level()

screen.exitonclick()
