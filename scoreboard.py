from turtle import Turtle

# Constants
ALIGNMENT = 'center'
FONT = ('Courier', 20, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.color('magenta')
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

