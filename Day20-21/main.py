import time
from turtle import Screen
from food import Food
from scoreboard import Scorecard


from snake import Snake

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.title('Snake Game')
# it will help me by turing off the animations and update the screen only when i do so
screen.tracer(0)

snake = Snake()
food = Food()
scorecard = Scorecard()

screen.listen()

screen.onkey(key='Up', fun=snake.move_up)
screen.onkey(key='Down', fun=snake.move_down)
screen.onkey(key='Left', fun=snake.move_left)
screen.onkey(key='Right', fun=snake.move_right)

game_is_on = True

while game_is_on:
    screen.update()
    # we turned off the animations to use our own.
    # time.sleep() is used to hide the background work for specific time frame
    time.sleep(0.1)
    snake.move_snake()

    # detect collision with food
    if snake.head.distance(food) < 15:
        scorecard.increase_score()
        food.refresh()
        snake.extend_snake()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scorecard.game_over()

    # detect collision with tail
    # if head collides with any segment
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scorecard.game_over()

screen.exitonclick()
