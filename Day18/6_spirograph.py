import random
import turtle as t

my_turtle = t.Turtle()
my_turtle.pensize(1)
t.colormode(255)
my_turtle.speed('fastest')


def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    return (r, g, b)


def draw_spirograph(gap):
    for i in range(int(360/gap)):
        my_turtle.color(random_color())
        my_turtle.circle(100)
        my_turtle.setheading(my_turtle.heading() + gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick
