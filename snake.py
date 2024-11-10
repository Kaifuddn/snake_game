from tkinter.constants import RIGHT
from turtle import Turtle

STARTING_SEGMENT  = [(0,0) , (-20,0) , (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 180
LEFT = 270
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_SEGMENT:
            snap = Turtle(shape="square")
            snap.color("white")
            snap.penup()
            snap.goto(position)
            self.segments.append(snap)

    def move(self):
        for seg_num in range(len(self.segments)- 1, 0, -1):
            new_x = self.segments[seg_num].xcor()
            new_y = self.segments[seg_num].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)