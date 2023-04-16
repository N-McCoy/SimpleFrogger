from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.allcars = []
        self.speed = 0

    def make_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle('square')
            car.penup()
            car.shapesize(stretch_len=2)
            car.color(random.choice(COLORS))
            car.goto(300, random.randint(-250, 260))
            car.setheading(180)
            self.allcars.append(car)


    def car_move(self):
        for car in self.allcars:
            car.forward(STARTING_MOVE_DISTANCE + self.speed)


    def upgrade_cars(self):
        self.speed += MOVE_INCREMENT
        for car in self.allcars:
            car.hideturtle()
