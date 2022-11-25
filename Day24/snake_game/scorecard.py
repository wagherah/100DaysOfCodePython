from turtle import Turtle


class Scorecard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('snake_game/data.txt', mode='r+') as data:

            self.high_score = int(data.read())
        self.color('white')
        self.penup()
        self.goto(0, 280)

        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            arg=f"Score = {self.score} High Score = {self.high_score}",  align='center')

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('snake_game/data.txt', 'w') as data:
                data.write(f'{self.high_score}')

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg='Game Over', align='center')

    def increase_score(self):
        self.score = self.score + 1
        self.clear()
        self.update_scoreboard()
