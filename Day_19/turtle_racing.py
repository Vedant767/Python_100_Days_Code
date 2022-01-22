from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height= 400)

is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")

colors = ["blue", "green", "yellow", "orange", "red", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for index in range(0, 6):
    jack = Turtle(shape="turtle")
    jack.color(colors[index])
    jack.up()
    jack.goto(x=-230, y=y_positions[index])
    all_turtles.append(jack)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost', The {winner} turtle is the winner!")
            is_race_on = False
        
        get_steps = random.randint(0, 10)
        turtle.forward(get_steps)
        

screen.exitonclick()