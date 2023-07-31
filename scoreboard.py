from turtle import Turtle
font = ("Arial", 24, "normal") # set font
align = "center" # set alignment
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0 # set score
        self.color("white") # set color
        self.penup() # pen up
        self.goto(0, 270) # set position
        self.hideturtle() # hide turtle
        self.update_scoreboard() # update scoreboard
    
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=align, font=font) # write score
    
    def increase_score(self):
        self.score += 1
        self.clear() # clear previous score
        self.update_scoreboard() # update scoreboard
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=align, font=font) # write game over
        self.update_scoreboard() # update scoreboard