import turtle
from main import SCREEN_SIZE_XY_PX

FONT_TYPE = "Arial"
FONT_SIZE = 20
FONT_STYLE = "normal"


class Scoreboard(turtle.Turtle):

    def __init__(self, color):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as datafile:
            self.highscore = int(datafile.read())
        self.penup()
        self.color(color)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write_score()
        self.write_highscore()

    def write_score(self):
        x_position = 0
        y_position = SCREEN_SIZE_XY_PX / 2 - 2 * FONT_SIZE
        self.goto(x_position, y_position)
        self.write(arg=f"Score:{self.score}", align="center", font=(FONT_STYLE, FONT_SIZE, FONT_STYLE))

    def write_highscore(self):
        x_position = 0
        y_position = SCREEN_SIZE_XY_PX / 2 - 3 * FONT_SIZE
        self.goto(x_position, y_position)
        self.write(arg=f"Highscore:{self.highscore}", align="center",
                   font=(FONT_STYLE, round(FONT_SIZE / 2), FONT_STYLE))

    def increase_score(self):
        self.score += 1

    def update_highscore(self):
        if self.score > self.highscore:
            with open("data.txt", mode="w") as datafile:
                datafile.write(str(self.score))
            self.highscore = int(self.score)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over!", align="center", font=(FONT_STYLE, FONT_SIZE * 2, FONT_STYLE))

    def reset_score(self):
        self.score = 0
