import random
from turtle import Turtle

SHAPE = "circle"
COLOR = "blue"
# l2 = ["red", "orange", "yellow", "green", "blue", "purple"]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        # this is a size of a circle(food)
        self.shapesize(0.9, 0.9)
        self.penup()
        self.color(COLOR)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        xaxis = random.randint(-250, 250)
        yaxis = random.randint(-250, 250)
        self.goto(xaxis, yaxis)
