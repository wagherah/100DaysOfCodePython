# Notes
# Turtle Event Listener
# To note what user does. e.g
# 1. What he presses.

# The code that allows us to do this are called listeners


from turtle import Screen, Turtle


my_turtle = Turtle()
screen = Screen()


def move_forward():
    my_turtle.forward(10)


def move_backward():

    my_turtle.backward(10)


def turn_right():
    my_turtle.setheading(my_turtle.heading() - 10)


def turn_left():
    my_turtle.setheading(my_turtle.heading() + 10)


def clear_drawing():

    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()


# in order to listen to the events, we need listen method of the screen object
screen.listen()

# it will bind function to a specific key
# onkey(fun, key)
# These functions are called higher order functions as they works with another functions
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")

screen.onkey(fun=clear_drawing, key="c")


screen.exitonclick()
