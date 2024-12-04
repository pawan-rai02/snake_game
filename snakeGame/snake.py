from turtle import Screen, Turtle
import random
HEAD_COLOR = ["red", "purple", "pink", "green", "orange", "yellow" , "blue"]
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
COLORS = ["red", "purple", "pink", "green", "orange", "yellow" , "blue"]
rand_color = random.choice(COLORS)
class Snake:

    def __init__(self):
        self.all_turtle = []
        self.create_snake()
        self.head = self.all_turtle[0]
        self.rand = random.choice(HEAD_COLOR)
        self.head.color(self.rand)


    def create_snake(self):
        for position in STARTING_POS:
            self.add_segment(position)



    def add_segment(self,position):
        new_turtle = Turtle('square')
        new_turtle.penup()
        new_turtle.color(rand_color)
        new_turtle.goto(position)
        self.all_turtle.append(new_turtle)

    def reset(self):
        for seg in self.all_turtle:
            seg.goto(1000, 1000)
        self.all_turtle.clear()
        self.create_snake()
        self.head = self.all_turtle[0]
        self.head.color("red")

    def extend(self):
        self.add_segment(self.all_turtle[-1].position())
    def  move(self):
        for seg_num in range(len(self.all_turtle) - 1, 0, -1):
            x_coor = self.all_turtle[seg_num - 1].xcor()
            y_coor = self.all_turtle[seg_num - 1].ycor()
            self.all_turtle[seg_num].goto(x=x_coor, y=y_coor)
        self.head.forward(MOVE_DIST)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)



    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

