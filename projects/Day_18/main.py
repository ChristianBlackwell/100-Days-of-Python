import random
import turtle as t
from turtle import Turtle, Screen

timmy = Turtle()
t.colormode(255)
timmy.shape("turtle")
timmy.speed("fastest")
timmy.hideturtle()
timmy.penup()

#Drawing Dots - Final Iteration
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random_color())
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

''' Drawing Dots - First Iteration
def dotted_line():
    timmy.dot(10, random_color())
    for _ in range(9):
        timmy.penup()
        timmy.fd(50); timmy.dot(20, random_color())

def turn_left():
    timmy.lt(90)
    timmy.fd(50)
    timmy.lt(90)

def turn_right():
    timmy.rt(90)
    timmy.fd(50)
    timmy.rt(90)

def make_art():
    for _ in range(5):
        dotted_line()
        turn_left()
        dotted_line()
        turn_right()

timmy.home()
make_art()'''




'''Make a Spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)
draw_spirograph(5)'''

'''Random Walk
direcions = [0, 90, 180, 270]

for i in range(200):
    timmy.fd(30)
    timmy.setheading(random.choice(direcions))
    timmy.color(random_color())'''

'''First Random Walk Iteration - *OLD*
for i in range(200):
    steps = int(random.random() * 30)
    angle = int(random.random() * 360)
    timmy.color(random.choice(colors))
    timmy.right(angle)
    timmy.fd(steps)'''

'''Draw Shapes - Triangle to Decagon
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.fd(100)
        timmy.rt(angle)

for shape_side_n in range(3, 11):
    timmy.color(random.choice(colors))
    draw_shape(shape_side_n)'''

screen = Screen()
screen.exitonclick()