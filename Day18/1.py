from turtle import Screen, Turtle
import turtle

# it will create an instance of turtle which will flash for a while
timmy_the_turtle = Turtle()


turtle.shape('square')
turtle.color('blue')

# in order to make the window stay, we need to,
# it should be in the end
screen = Screen()
screen.exitonclick()
