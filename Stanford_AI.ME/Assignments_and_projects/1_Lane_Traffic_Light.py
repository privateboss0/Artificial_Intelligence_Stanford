import turtle
import time

window = turtle.Screen()
window.title("1 lane traffic light")
window.bgcolor("black")
window.tracer(0)

pen = turtle.Turtle()
pen.color("yellow")
pen.width(3)
pen.speed(6)
pen.hideturtle()
pen.penup()

# Draw the first box
pen.goto(-30, 90)
pen.pendown()
for side in range(4):
    pen.forward(90)
    pen.right(90)
pen.penup()

# Move the turtle down and draw the second box
pen.goto(-30, 00)
pen.pendown()
for side in range(4):
    pen.forward(90)
    pen.right(90)
pen.penup()

# Move the turtle down and draw the third box
pen.goto(-30, -90)
pen.pendown()
for side in range(4):
    pen.forward(90)
    pen.right(90)
pen.penup()

def draw_circle(x, y, size, fill, color):
    if fill != "":
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color(color)
        turtle.begin_fill()
        turtle.circle(size)
        turtle.end_fill()

def turn_off_red_light():
  draw_circle(15, 15, 30, "grey", "black")

def turn_off_green_light():
  draw_circle(15, -160, 30, "grey", "black")

def turn_off_yellow_light():
  draw_circle(15, -75, 30, "grey", "black")

# This variable holds the current state of the machine
light_box_state = ""

# Set timers for the light durations
window.ontimer(lambda: draw_circle(15, 15, 30, "black", ""), )
window.ontimer(lambda: draw_circle(15, -75, 30, "black", ""), )
window.ontimer(lambda: draw_circle(15, -160, 30, "black", ""), )

# Call the state machine every 1000 milliseconds
def advanced_state_machine():

  global light_box_state

  draw_circle(15, 15, 30, "black", "")
  draw_circle(15, -75, 30, "black", "")
  draw_circle(15, -160, 30, "black", "")

  if light_box_state == "green":
    turn_off_red_light()
    turn_off_yellow_light()

  if light_box_state =="red":
    turn_off_green_light()
    turn_off_yellow_light()

  if light_box_state == "yellow":
    turn_off_green_light()
    turn_off_red_light()

  # Turn on the light for the red state.
  if light_box_state == "red":
    draw_circle(15, 15, 30, "black", "red")
    draw_circle(15, -75, 30, "black", "")
    draw_circle(15, -160, 30, "black", "")
    time.sleep(3) #Stimulating approximately 30seconds
    light_box_state = "green"

# Turn on the light for the green state.
  elif light_box_state == "green":
    draw_circle(15, 15, 30, "black", "")
    draw_circle(15, -75, 30, "black", "")
    draw_circle(15, -160, 30, "black", "green")
    time.sleep(6) #Stimulating approximately 60seconds
    light_box_state = "yellow"
  
  # Turn on the light for the yellow state.
  else:
    light_box_state = "yellow"
    draw_circle(15, 15, 30, "black", "")
    draw_circle(15, -75, 30, "black", "yellow")
    draw_circle(15, -160, 30, "black", "")
    time.sleep(9) #Stimulating approximately 90seconds
    light_box_state = "red"

  window.ontimer(advanced_state_machine, 2000)
advanced_state_machine()
window.mainloop()