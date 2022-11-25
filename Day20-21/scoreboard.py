

from turtle import Turtle

# SCORE = 0


class Scorecard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 280)

        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg='Score =' + str(self.score),  align='center')

    def game_over(self):
        self.goto(0,0)
        self.write(arg='Game Over', align='center')

    def increase_score(self):
        self.score = self.score + 1
        self.clear()
        self.update_scoreboard()
