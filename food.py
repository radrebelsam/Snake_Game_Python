from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle") # set shape
        self.penup # don't draw line
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # set size
        self.speed("fastest") # set speed
        self.goto(random.randint(-280, 280), random.randint(-280, 280)) # set position
    
    def refresh(self):
        self.pos = (random.randint(-280, 280), random.randint(-280, 280)) # set position