import random
import turtle as t


my_turtle = t.Turtle()
my_turtle.pensize(15)
my_turtle.speed('slow')
t.colormode(255)

directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    return (r, g, b)


for i in range(1000):
    my_turtle.color(random_color())
    my_turtle.forward(100)
    my_turtle.setheading(random.choice(directions))


screen = t.Screen()
screen.exitonclick()
