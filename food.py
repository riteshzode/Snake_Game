import random
from turtle import Turtle

SHAPE = "circle"
COLOR = "blue"
color_list = ["red", "orange", "yellow", "green", "blue", "purple"]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.shapesize(0.9, 0.9)
        self.penup()
        self.color(COLOR)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        xaxis = random.randint(-250, 250)
        yaxis = random.randint(-250, 250)
        self.color(random.choice(color_list))
        self.goto(xaxis, yaxis)
