import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.onkeypress(player.move_up, "Up")
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move_car()

    # Detect collision with finish line
    if player.is_touch_finish_line():
        player.reset_player_position()
        scoreboard.increase_level()
        car_manager.increase_car_speed()

    # Detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 10:
            game_is_on = False
            scoreboard.game_over()
    screen.update()



screen.exitonclick()