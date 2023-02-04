import random
from car import Car


class CarControl:
    def __init__(self, number_of_cars, screen_width, screen_height):
        self.number_of_cars = number_of_cars
        self.cars = []
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.generate_cars()

    def generate_cars(self):
        for car_number in range(0, self.number_of_cars):
            self.cars.append(Car(self.screen_width, self.screen_height))

    def move_cars(self):
        for car_number in range(0, self.number_of_cars):
            self.cars[car_number].drive()

    def increase_cars_speed(self):
        for car_number in range(0, self.number_of_cars):
            self.cars[car_number].activate_turbo()

    def reset_cars_speed(self):
        for car_number in range(0, self.number_of_cars):
            self.cars[car_number].reset_drive_speed()
