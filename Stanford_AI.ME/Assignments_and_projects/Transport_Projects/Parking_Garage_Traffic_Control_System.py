import turtle
import time

window = turtle.Screen()
window.title("ParkingGarage Traffic Light")
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

def draw_circle(x, y, size, fill, color):
    if fill != "":
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color(color)
        turtle.begin_fill()
        turtle.circle(size)
        turtle.end_fill()

def turn_off_green_light():
  draw_circle(15, 15, 30, "grey", "black")

def turn_off_red_light():
  draw_circle(15, 15, 30, "grey", "black")

# This variable holds the current state of the machine
light_box_state = ""

window.ontimer(lambda: draw_circle(15, 15, 30, "grey", "red"))
def advanced():
  global light_box_state

  draw_circle(15, 15, 30, "", "")

  if light_box_state =="green":
      turn_off_red_light()
      draw_circle(15, 15, 30, "grey", "green")
      time.sleep(7) #Simulating 50 seconds for red light
      light_box_state = "red"

  else:
    light_box_state == "red"
    turn_off_green_light()
    draw_circle(15, 15, 30, "grey", "red")
    time.sleep(15) #Simulating 100 seconds for green light
    light_box_state = "green"

  window.ontimer(advanced, 2000)
advanced()
window.mainloop()
