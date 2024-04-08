import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle()
            new_car.shape('square')
            new_car.penup()
            new_car.setheading(180)
            new_car.shapesize(stretch_wid=1, stretch_len=3)
            coordinates = [(280, 0), (280, 100), (280, 200), (280, 240), (280, -100), (280, -200)]
            new_car.goto(random.choice(coordinates))
            new_car.color(random.choice(COLORS))
            self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
