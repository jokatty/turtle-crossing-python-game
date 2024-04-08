from turtle import Screen
import time
from player import Player
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# initiate player
player = Player()

# listen for the key press
screen.listen()
screen.onkey(player.move, "Up")

# create car object
car = CarManager()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.generate_car()
    car.move_car()



