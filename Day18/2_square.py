from turtle import Screen, Turtle

myturtle = Turtle()

for i in range(4):
    myturtle.forward(100)
    myturtle.right(90)


screen = Screen()
screen.exitonclick()
