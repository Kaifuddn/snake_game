from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,270)
        self.write(f"Score : {self.score}", align="center" , font=("Courier", 20, "normal"))
        self.penup()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center" , font=("Courier", 40, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=("Courier", 20, "bold"))

