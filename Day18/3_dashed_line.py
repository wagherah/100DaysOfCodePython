from turtle import Screen, Turtle

my_turtle = Turtle()

for i in range(20):
    my_turtle.forward(10)
    my_turtle.penup()
    my_turtle.forward(10)
    my_turtle.pendown()


screen = Screen()
screen.exitonclick()
