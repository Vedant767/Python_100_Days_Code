from turtle import *

josh = Turtle()
josh.shape("turtle")
josh.color("red","black")

for _ in range(20):
    josh.pendown()
    josh.forward(10)
    josh.penup()
    josh.forward(10)

screen = Screen()
screen.exitonclick()

