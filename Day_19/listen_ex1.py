from turtle import Turtle, Screen, forward

jack = Turtle()
screen = Screen()

def move_forward():
    jack.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()