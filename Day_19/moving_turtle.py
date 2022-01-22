from turtle import Turtle, Screen

jack = Turtle()
screen = Screen()

def move_forward():
    jack.forward(10)

def move_backward():
    jack.backward(10)

def move_left():
    jack.lt(10)

def move_right():
    jack.rt(10)

def clear():
    jack.clear()
    jack.up()
    jack.home()
    jack.down()

screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")

screen.onkeypress(clear, "c")

screen.listen()

screen.exitonclick()