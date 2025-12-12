from turtle import Turtle, Screen
import random

#Screen / Game Setup
is_racing = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter one of the following colors: Blue, Red, Green, Orange, Black, Purple, Pink")
colors = ["Blue", "Green", "Red", "Orange", "Black", "Purple", 'Pink']
y_positions = [-150, -100, -50, 0, 50, 100, 150]
all_turtles = []

#Turtle(s) Creation / Setup
for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_racing = True

while is_racing:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_racing = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} turtle has won the race!")
            else:
                print(f"You've lost. The {winning_turtle} turtle has won the race.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

'''Etch a Sketch - First & Final Iteration
timmy = Turtle()
screen.listen()
def move_forward():
    timmy.forward(10)
def move_backward():
    timmy.backward(10)
def turn_left():
    timmy.left(10)
def turn_right():
    timmy.right(10)
def reset():
    timmy.reset()

screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=reset, key="c")'''

screen.exitonclick()