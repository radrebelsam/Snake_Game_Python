from turtle import Turtle, Screen
import time
import snake
import food
import scoreboard


# set screen
screen = Screen() # create screen
screen.setup(width=600, height=600) # set screen size
screen.bgcolor("black") # set background color
screen.title("Snake Game") # set title
screen.tracer(0) # turn off animation


snake = Snake() # create snake object
food = Food() # create food object
scoreboard = Scoreboard() # create scoreboard object


screen.listen() # listen to key strokes
screen.onkey(snake.up(), "Up") # move snake up
screen.onkey(snake.down(), "Down") # move snake down
screen.onkey(snake.left(), "Left") # move snake left
screen.onkey(snake.right(), "Right") # move snake right


# make snake move continuously
game_is_on = True
while game_is_on:
    screen.update() # update all segments together on screen
    time.sleep(1) # delay 1 second
    snake.move() # move snake
    
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
    
    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()





screen.exitonclick() # exit screen on click
