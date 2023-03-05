from turtle import Turtle
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for i in STARTING_POS:
            self.add_segment(i)

    def add_segment(self, pos):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(pos)
        self.segment.append(new_segment)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)

        self.head.forward(20)

    # def right(self):
    #     for seg_num in range(len(self.segment) - 1, 0, -1):
    #         new_x = self.segment[seg_num - 1].xcor()
    #         new_y = self.segment[seg_num - 1].ycor()
    #         self.segment[seg_num].goto(new_x, new_y)
    #
    #     direction = self.head.heading()
    #     self.head.setheading(direction-90)
    #     self.head.forward(20)
    #
    # def left(self):
    #     for seg_num in range(len(self.segment) - 1, 0, -1):
    #         new_x = self.segment[seg_num - 1].xcor()
    #         new_y = self.segment[seg_num - 1].ycor()
    #         self.segment[seg_num].goto(new_x, new_y)
    #
    #     direction = self.head.heading()
    #     self.head.setheading(direction+90)
    #     self.head.forward(20)

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

    def reset(self):
        for seg in self.segment:
            seg.goto(x=1500, y=1500)

        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]
