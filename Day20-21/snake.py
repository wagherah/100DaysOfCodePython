from turtle import Turtle


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        my_turtle = Turtle('square')
        my_turtle.color('white')
        my_turtle.penup()
        my_turtle.goto(position)
        self.segments.append(my_turtle)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def move_snake(self):
        # we will move the snake by getting hold of the first segment
        # we will move the last segment to the second last's place and second segment to the first place
        for seg in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg-1].xcor()
            new_y = self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)
        # self.segments[0].right(90)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
