from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.fetch_high_score()
        self.goto(0, 265)
        self.color("white")
        self.ht()
        self.write_score()
    
    def cal_score(self):
        self.score = self.score + 1
        self.clear()
        self.write_score()
    
    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score= self.score
            self.save_high_score(f"{self.high_score}")
        self.score = 0
        self.write_score()
    
    def save_high_score(self, score):
        with open("highscore.txt", mode='w') as file:
            file.write(score)

    def fetch_high_score(self):
        with open("highscore.txt") as file:
            return int(file.read())
    
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", False, align="center", font=FONT)