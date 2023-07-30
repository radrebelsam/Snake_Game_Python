from turtle import Turtle, Screen
import time

# set screen
screen = Screen() # create screen
screen.setup(width=1200, height=1200) # set screen size
screen.bgcolor("black") # set background color
screen.title("Snake Game") # set title
screen.tracer(0) # turn off animation


# create snake body
# set starting position
starting_position = [(0, 0), (-20, 0), (-40, 0)]
# create snake body segments
segments = []
for position in starting_position:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.goto(position)


# make snake move continuously
game_is_on = True
while game_is_on:
    
    screen.update() # update all segments together on screen
    time.sleep(1) # delay 1 second
    
    # make 2nd and 3rd segment follow previous segment
    for i in range(start=len(segments)-1, stop=0, step=-1):
        segments[i].goto(segments[i-1].xcor(), segments[i-1].ycor())
    
    
    segments[0].forward(20) # move 1st segment
    
    







screen.exitonclick() # exit screen on click
