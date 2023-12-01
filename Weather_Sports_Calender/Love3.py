import turtle
from turtle import *

def draw_black_heart():
    t.color("black")
    t.begin_fill()
    t.pensize(3)
    t.left(50)
    t.forward(133)
    t.circle(50, 200)
    t.right(140)
    t.circle(50, 200)
    t.forward(133)
    t.end_fill()

def draw_gold_heart():
    t.color("gold")
    t.begin_fill()
    t.pensize(3)
    t.left(50)
    t.forward(133)
    t.circle(50, 200)
    t.right(140)
    t.circle(50, 200)
    t.forward(133)
    t.end_fill()

def draw_yellow_heart():
    t.color("yellow")
    t.begin_fill()
    t.pensize(3)
    t.left(50)
    t.forward(133)
    t.circle(50, 200)
    t.right(140)
    t.circle(50, 200)
    t.forward(133)
    t.end_fill()

t = turtle.Turtle()
t.speed(0)

# Draw the black heart
draw_black_heart()

# Move the turtle to the position for the black heart
t.penup()
t.setheading(0)
t.goto(-270, 0)
t.pendown()

# Draw the gold heart
draw_gold_heart()

# Move the turtle to the position for the yellow heart
t.penup()
t.setheading(0)
t.goto(270, 0)
t.pendown()

# Draw the yellow heart
draw_yellow_heart()

turtle.Screen().mainloop()