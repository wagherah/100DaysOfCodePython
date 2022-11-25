# import colorgram

# colors = colorgram.extract('image.jpg', 10)

# rgb_colors = []

# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     color = (r,g,b)
#     rgb_colors.append(color)

# print(rgb_colors)
# we extracted the colors from the image

import random
import turtle as Turtle

my_turtle = Turtle.Turtle()
Turtle.colormode(255)
my_turtle.penup()
my_turtle.hideturtle()


color_list = [
    (245, 243, 238),
    (246, 242, 244),
    (202, 164, 110),
    (240, 245, 241),
    (236, 239, 243),
    (149, 75, 50),
    (222, 201, 136),
    (53, 93, 123),
    (170, 154, 41),
    (138, 31, 20),
]

my_turtle.setheading(225)
my_turtle.forward(300)
my_turtle.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    my_turtle.dot(20, random.choice(color_list))
    my_turtle.forward(50)

    if dot_count % 10 == 0:
        my_turtle.setheading(90)
        my_turtle.forward(50)
        my_turtle.setheading(180)
        my_turtle.forward(500)
        my_turtle.setheading(0)


screen = Turtle.Screen()
screen.exitonclick()
