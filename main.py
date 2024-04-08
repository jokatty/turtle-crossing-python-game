from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# initiate player
player = Player()

# listen for the key press
screen.listen()
screen.onkey(player.move, "Up")

# create car object
car_manager = CarManager()

score_board = ScoreBoard((-280, 250))
score_board.display_level()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.generate_car()
    car_manager.move_car()
    for car in car_manager.cars:
        if player.distance(car) < 30:
            game_is_on = False
            game_status = ScoreBoard((0, 0))
            game_status.game_over()

    if player.restart:
        car_manager.level_up()
        score_board.update_level()
        player.restart = False

screen.exitonclick()


