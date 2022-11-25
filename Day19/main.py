from turtle import Screen, Turtle
import random as random


race_is_on = False

screen = Screen()
# sets up the screen length and width
screen.setup(width=500, height=400)

colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']

all_turtles = []


user_input = screen.textinput(
    title='Python Turtle', prompt='Select Your Turtle')

if user_input:
    race_is_on = True

y = -100
for i in range(6):
    my_turtle = Turtle('turtle')
    my_turtle.color(colors[i])
    my_turtle.penup()
    my_turtle.goto(x=-230, y=y)
    y = (y + 50)
    all_turtles.append(my_turtle)

while race_is_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            race_is_on = False
            winner = turtle.pencolor()

            if winner == user_input:

                print('You have won. The ' + winner + ' is the winner')

            else:

                print('You have lost. The ' + winner + ' is the winner')

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
