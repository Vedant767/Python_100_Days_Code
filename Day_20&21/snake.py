from turtle import Turtle

STARTING_POSITION = [(0,0), (-20, 0), (-40, 0)]
MOVE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self) -> None:
        self.parts = []
        self.create()
        self.head = self.parts[0]

    def create(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
    
    def add_segment(self, position):
        part1 = Turtle("square")
        part1.color("white")
        part1.penup()
        part1.goto(position)
        self.parts.append(part1)
    
    def extend(self):
        self.add_segment(self.parts[-1].position())

    def move(self):
        for i in range(len(self.parts) - 1, 0, -1):
            new_x = self.parts[i - 1].xcor()
            new_y = self.parts[i - 1].ycor()
            self.parts[i].goto(new_x, new_y) 
        self.head.forward(MOVE)
    
    def right(self):
        if self.head.heading() != LEFT: 
            self.head.setheading(RIGHT)
    
    def up(self):
        if self.head.heading() != DOWN: 
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT: 
            self.head.setheading(LEFT)
    
    def down(self):
        if self.head.heading() != UP: 
            self.head.setheading(DOWN)
    
    def reset(self):
        for part in self.parts:
            part.goto(1000, 1000)
        self.parts.clear()
        self.create()
        self.head = self.parts[0]


