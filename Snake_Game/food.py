from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.move()
#* Earlier I left it as same as food move This led to no activity in GUi

    def move(self):
        random_x = random.randint(-200,200)
        random_y = random.randint(-200, 200)
        self.goto(random_x, random_y)
