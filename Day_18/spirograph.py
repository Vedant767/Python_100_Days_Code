from turtle import Screen, Turtle, colormode
import random

josh = Turtle()

josh.pensize(4)
josh.speed(0)
colormode(255)

def random_color():
    josh.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))

def draw_circle(angle):
    for _ in range(int(360 / angle)):
        random_color()
        josh.circle(120)
        josh.setheading(josh.heading() + angle)
    
draw_circle(10)

screen = Screen()
screen.exitonclick()