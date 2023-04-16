import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
carManager = CarManager()
level = Scoreboard()

screen.listen()
screen.onkeypress(player.move_forward, 'w')

game_is_on = True
while game_is_on:
    carManager.make_car()
    carManager.car_move()
    time.sleep(0.1)
    screen.update()

    if player.ycor() > 280:
        carManager.upgrade_cars()
        level.change_level()
        player.go_to_start()

    for car in carManager.allcars:
        if car.distance(player) < 20:
            level.game_over()
            game_is_on = False


screen.exitonclick()