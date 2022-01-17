from turtle import Screen, Turtle
import random

josh = Turtle()
colours = ["red", "blue", "green", "yellow"]

def draw_shapes(no_of_sides):
    angle = 360 / no_of_sides
    for _ in range(no_of_sides):
        josh.right(angle)
        josh.forward(100)


for angle in range(3, 11):
    josh.pencolor(random.choice(colours))
    draw_shapes(angle)

screen = Screen()
screen.exitonclick()