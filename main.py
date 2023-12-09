from turtle import Turtle, Screen
from random import randint
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "blue", "green", "yellow", "pink"]
turtles = []


def draw_finish_line():
    finish_line = Turtle()
    finish_line.hideturtle()
    finish_line.pensize(3)
    finish_line.penup()
    finish_line.goto(220, 200)
    finish_line.right(90)
    for i in range(0, 20):
        finish_line.pendown()
        finish_line.forward(10)
        finish_line.penup()
        finish_line.forward(10)


def set_turtles():
    for color in colors:
        turtle = Turtle(shape="turtle")
        turtle.color(color)
        turtles.append(turtle)

    nr = 1
    for turtle in turtles:
        turtle.penup()
        turtle.goto(-230, 190 - 50 * nr)
        nr += 1


def start_race():
    still_racing = True
    while still_racing:
        for turtle in turtles:
            turtle.forward(randint(0,10))
            if turtle.xcor() > 225:
                still_racing = False
                winner = turtle.pencolor()
    if winner == user_bet:
        print(f"You won the bet!")
    else:
        print(f"You lost te bet! The winner turtle is {winner}")


draw_finish_line()
set_turtles()
start_race()
screen.exitonclick()
