from turtle import Turtle

FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_Scoreboard()
                
    def update_Scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_Scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)