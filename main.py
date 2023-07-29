from turtle import Turtle, Screen


# set screen
screen = Screen() # create screen
screen.setup(width=600, height=600) # set screen size
screen.bgcolor("black") # set background color
screen.title("Snake Game") # set title
# exit screen on click


# create snake body method 1
""" block_1 = Turtle(shape="square")
block_1.color("white")
block_2 = Turtle(shape="square")
block_2.color("white")
block_2.goto(-20, 0)
block_3 = Turtle(shape="square")
block_3.color("white")
block_3.goto(-40, 0) """


# create snake body method 2
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
    for segment in segments:
        segment.forward(20)





