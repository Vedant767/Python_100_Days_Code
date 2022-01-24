from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 265)
        self.color("white")
        self.ht()
        self.write_score()
    
    def cal_score(self):
        self.score = self.score + 1
        self.clear()
        self.write_score()
    
    def write_score(self):
        self.write(f"Score: {self.score}", False, align="center", font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, align="center", font=FONT)