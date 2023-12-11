#This program allows the centralized asynchronous control of vehicles for a three lane road
import turtle
import time

window = turtle.Screen()
window.title("Centralized Asynchronous Traffic Light")
window.bgcolor("black")
window.tracer(0)

pen = turtle.Turtle()
pen.color("yellow")
pen.width(3)
pen.speed(6)
pen.hideturtle()
pen.penup()

# Draw the first box middle light
pen.goto(-15, 90)
pen.pendown() 
for side in range(4):
    pen.forward(90)
    pen.right(90)
pen.penup()

# Draw the second box middle light
pen.goto(-15, 00)
pen.pendown()
for side in range(4):
    pen.forward(90)
    pen.right(90)
pen.penup()

# Draw the third box middle light
pen.goto(-15, -90)
pen.pendown()
for side in range(4):
    pen.forward(90)
    pen.right(90)
pen.penup()

# Draw the first box right light
pen.goto(120, 90)
pen.pendown() 
for side in range(4):
    pen.forward(90)
    pen.right(90)
pen.penup()

# Draw the second box right light
pen.goto(120, 00)
pen.pendown()
for side in range(4):
    pen.forward(90)
    pen.right(90)
pen.penup()

# Draw the third box right light
pen.goto(120, -90)
pen.pendown()
for side in range(4):
    pen.forward(90)
    pen.right(90)
pen.penup()

# Draw the first box left light
pen.goto(-150, 90)
pen.pendown() 
for side in range(4):
    pen.forward(90)
    pen.right(90)
pen.penup()

# Draw the second box left light
pen.goto(-150, 00)
pen.pendown()
for side in range(4):
    pen.forward(90)
    pen.right(90)
pen.penup()

# Draw the third box left light
pen.goto(-150, -90)
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

def turn_off_red_light0():
  draw_circle(30, 15, 30, "grey", "black")

def turn_off_red_light1():
  draw_circle(165, 15, 30, "grey", "black")

def turn_off_red_light2():
  draw_circle(-105, 15, 30, "grey", "black")

def turn_off_green_light0():
  draw_circle(30, -160, 30, "grey", "black")

def turn_off_green_light1():
  draw_circle(165, -160, 30, "grey", "black")

def turn_off_green_light2():
  draw_circle(-105, -160, 30, "grey", "black")

def turn_off_yellow_light0():
  draw_circle(30, -75, 30, "grey", "black")

def turn_off_yellow_light1():
  draw_circle(165, -75, 30, "grey", "black")

def turn_off_yellow_light2():
  draw_circle(-105, -75, 30, "grey", "black")

# This variable is a placeholder for the current state of lights
light_box_state0 = ""
light_box_state1 = ""
light_box_state2 = ""

# Set timers for the light durations
window.ontimer(lambda: draw_circle(30, 15, 30, "black", ""), )
window.ontimer(lambda: draw_circle(30, -75, 30, "black", ""), )
window.ontimer(lambda: draw_circle(30, -160, 30, "black", ""), )

# Set timers for the light durations
window.ontimer(lambda: draw_circle(165, 15, 30, "black", ""), )
window.ontimer(lambda: draw_circle(165, -75, 30, "black", ""), )
window.ontimer(lambda: draw_circle(165, -160, 30, "black", ""), )

# Set timers for the light durations
window.ontimer(lambda: draw_circle(-105, 15, 30, "black", ""), )
window.ontimer(lambda: draw_circle(-105, -75, 30, "black", ""), )
window.ontimer(lambda: draw_circle(-105, -160, 30, "black", ""), )

def advanced_machine_state():
  global light_box_state0

  draw_circle(30, 15, 30, "black", "")
  draw_circle(30, -75, 30, "black", "")
  draw_circle(30, -160, 30, "black", "")

  if light_box_state0 == "green":
    turn_off_red_light0()
    turn_off_yellow_light0()

  if light_box_state0 =="red":
    turn_off_green_light0()
    turn_off_yellow_light0()

  if light_box_state0 == "yellow":
    turn_off_green_light0()
    turn_off_red_light0()

  # Turn on the light for the yellow state.
  if light_box_state0 == "red":
    draw_circle(30, 15, 30, "black", "red")
    draw_circle(30, -75, 30, "black", "")
    draw_circle(30, -160, 30, "black", "")
    time.sleep(3) #Stimulating approximately 30seconds for the middle amber light.
    
    light_box_state0 = "green"

# Turn on the light for the red state.
  elif light_box_state0 == "green":
    draw_circle(30, 15, 30, "black", "")
    draw_circle(30, -75, 30, "black", "")
    draw_circle(30, -160, 30, "black", "green")
    time.sleep(6) #Stimulating approximately 60seconds for the middle red light.
    
    light_box_state0 = "yellow"
  
  # Turn on the light for the green state.
  else:
    light_box_state0 == "yellow"
    draw_circle(30, 15, 30, "black", "")
    draw_circle(30, -75, 30, "black", "yellow")
    draw_circle(30, -160, 30, "black", "")
    time.sleep(9) #Stimulating approximately 90seconds for the middle green light.
    light_box_state0 = "red"

  window.ontimer(advanced_machine_state, 2000)
advanced_machine_state()

def state_machine_advanced():
  global light_box_state1

  draw_circle(165, 15, 30, "black", "")
  draw_circle(165, -75, 30, "black", "")
  draw_circle(165, -160, 30, "black", "")

  if light_box_state1 == "green":
    turn_off_red_light1()
    turn_off_yellow_light1()

  if light_box_state1 =="red":
    turn_off_green_light1()
    turn_off_yellow_light1()

  if light_box_state1 == "yellow":
    turn_off_green_light1()
    turn_off_red_light1()

  # Turn on the light for the yellow state.
  if light_box_state1 == "red":
    draw_circle(165, 15, 30, "black", "red")
    draw_circle(165, -75, 30, "black", "")
    draw_circle(165, -160, 30, "black", "")
    time.sleep(3) #Stimulating approximately 30seconds for right amber light.
    
    light_box_state1 = "green"

# Turn on the light for the red state.
  elif light_box_state1 == "green":
    draw_circle(165, 15, 30, "black", "")
    draw_circle(165, -75, 30, "black", "")
    draw_circle(165, -160, 30, "black", "green")
    time.sleep(6) #Stimulating approximately 60seconds for right red light.
    
    light_box_state1 = "yellow"
  
  # Turn on the light for the green state.
  else:
    light_box_state1 == "yellow"
    draw_circle(165, 15, 30, "black", "")
    draw_circle(165, -75, 30, "black", "yellow")
    draw_circle(165, -160, 30, "black", "")
    time.sleep(12) #Stimulating approximately 120seconds for right green light.
    light_box_state1 = "red"

  window.ontimer(state_machine_advanced, 2000)
state_machine_advanced()

def machine_state_advanced():
  global light_box_state2

  draw_circle(-105, 15, 30, "black", "")
  draw_circle(-105, -75, 30, "black", "")
  draw_circle(-105, -160, 30, "black", "")

  if light_box_state2 == "green":
    turn_off_red_light2()
    turn_off_yellow_light2()

  if light_box_state2 =="red":
    turn_off_green_light2()
    turn_off_yellow_light2()

  if light_box_state2 == "yellow":
    turn_off_green_light2()
    turn_off_red_light2()

  # Turn on the light for the yellow state.
  if light_box_state2 == "red":
    draw_circle(-105, 15, 30, "black", "red")
    draw_circle(-105, -75, 30, "black", "")
    draw_circle(-105, -160, 30, "black", "")
    time.sleep(3) #Stimulating approximately 30seconds for left amber light.
    
    light_box_state2 = "green"

# Turn on the light for the red state.
  elif light_box_state2 == "green":
    draw_circle(-105, 15, 30, "black", "")
    draw_circle(-105, -75, 30, "black", "")
    draw_circle(-105, -160, 30, "black", "green")
    time.sleep(7) #Stimulating approximately 70seconds for left red light.
    
    light_box_state2 = "yellow"
  
  # Turn on the light for the green state.
  else:
    light_box_state2 == "yellow"
    draw_circle(-105, 15, 30, "black", "")
    draw_circle(-105, -75, 30, "black", "yellow")
    draw_circle(-105, -160, 30, "black", "")
    time.sleep(15) #Stimulating approximately 150seconds for left green light.
    light_box_state2 = "red"

  window.ontimer(machine_state_advanced, 2000)
machine_state_advanced()  

window.mainloop()
