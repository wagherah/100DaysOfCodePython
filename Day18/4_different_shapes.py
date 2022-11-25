from turtle import Screen, Turtle

my_turtle = Turtle()


def draw_shapes(num_of_sides):
    angle = 360/num_of_sides
    for i in range(num_of_sides):
        my_turtle.right(angle)
        my_turtle.forward(100)


for i in range(3, 11):
    draw_shapes(i)


screen = Screen()
screen.exitonclick()
