from turtle import Turtle


starting_position = [(0, 0), (-20, 0), (-40, 0)] # set starting position
moving_distance = 20 # set moving distance
up = 90 # set up direction
down = 270 # set down direction
left = 180 # set left direction
right = 0 # set right direction

class Snake:
    def __init__(self):
        self.create_snake() # create snake body segments
        self.head = self.segments[0] # set head of snake
    
    def create_snake(self): # create snake body segments
        self.segments = []
        for position in starting_position:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)
            
    def move(self): # make snake move
        self.segments[0].forward(moving_distance) # move 1st segment
    
        # make 2nd and 3rd segment follow previous segment
        for i in range(start=len(self.segments)-1, stop=0, step=-1):
            self.segments[i].goto(self.segments[i-1].xcor(), self.segments[i-1].ycor())
    
    def up(self): # move snake up
        if self.head.heading() != down:
            self.head.setheading(up)
    
    def down(self): # move snake down
        if self.head.heading() != up:
            self.head.setheading(down)
    
    def left(self): # move snake left
        if self.head.heading() != right:
            self.head.setheading(left)
    
    def right(self): # move snake right
        if self.head.heading() != left:
            self.head.setheading(right)