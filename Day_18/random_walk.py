from turtle import Screen, Turtle, colormode
import random

josh = Turtle()

angle = [90, 180, 270, 360]

josh.pensize(20)
josh.speed(0)
colormode(255)

def draw():
    josh.setheading(random.choice(angle))
    josh.forward(50)
    josh.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))

for _ in range(200):
    draw()


screen = Screen()
screen.exitonclick()