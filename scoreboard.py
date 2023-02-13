from turtle import Turtle

with open("scoreboard.txt") as highest_score:
    score_text = int(highest_score.read())


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = score_text
        self.goto(0, 270)
        self.penup()
        self.color("white")
        self.update_score()
        self.hideturtle()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()

        self.goto(0, 0)
        self.write(f"Game Over!!", align="center", font=("Arial", 24, "normal"))

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))
        with open("scoreboard.txt", mode="w") as score:
            score.write(f"{self.high_score}")

    def increase_score(self):
        self.score += 1
        self.update_score()
