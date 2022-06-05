from turtle import Turtle

ALIGN = 'center'
FONT = ('Arial', 18, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=260)
        self.scoreupdate()

    def scoreupdate(self):
        self.clear()
        self.write(f"Your Score : {self.score} High Score : {self.high_score}", align=ALIGN, font=FONT)

    def high_score_update(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.scoreupdate()

    def scoreadd(self):
        self.score += 1
        self.scoreupdate()
