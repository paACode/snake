import turtle

FONT_TYPE = "Arial"
FONT_SIZE = 20
FONT_STYLE = "normal"


class Scoreboard(turtle.Turtle):

    def __init__(self, screensize, color):
        super().__init__()
        self.score = 0
        self.penup()
        self.color(color)
        self.hideturtle()
        self.x_position = 0
        self.y_position = screensize / 2 - 2 * FONT_SIZE
        self.goto(self.x_position, self.y_position)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Scoreboard:{self.score}", align="center", font=(FONT_STYLE, FONT_SIZE, FONT_STYLE))

    def increase_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over!", align="center", font=(FONT_STYLE, FONT_SIZE * 2, FONT_STYLE))
