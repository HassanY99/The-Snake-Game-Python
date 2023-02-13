from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

is_game_on = True

new_snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(new_snake.up, "Up")
screen.onkey(new_snake.down, "Down")
screen.onkey(new_snake.right, "Right")
screen.onkey(new_snake.left, "Left")

while is_game_on:
    screen.update()
    time.sleep(0.1)
    new_snake.move()

    if new_snake.head.distance(food) < 15:
        food.refresh()
        new_snake.extend()
        scoreboard.increase_score()

    if new_snake.head.xcor() > 280 or new_snake.head.xcor() < -280 or new_snake.head.ycor() > 280 \
            or new_snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.reset()

    for seg in new_snake.segments[1:]:
        if new_snake.head.distance(seg) < 10:
            is_game_on = False
            scoreboard.reset()


screen.exitonclick()
