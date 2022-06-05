import time
from turtle import Screen
from food import Food
from score import Score
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("MY SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.segments[0].distance(food) < 20:
        food.refresh()
        snake.extend()
        score.scoreadd()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.high_score_update()
        snake.snake_reset()


for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
        score.high_score_update()
        snake.snake_reset()

screen.exitonclick()
