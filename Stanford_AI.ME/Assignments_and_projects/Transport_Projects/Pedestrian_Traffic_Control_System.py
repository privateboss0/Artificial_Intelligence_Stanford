#https://pixabay.com/sound-effects/search/traffic-signal/ for blind pedestrian crossing sound
#This program allows disabled/wheelchair, blind, pedestrians, bikers, skaters etc. to cross the road safely.
import turtle
import time
from playsound import playsound

window = turtle.Screen()
window.title("Pedestrian Traffic Light")
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

# Draw the second box
pen.goto(-30, 00)
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

def play_alarm():
  playsound ('C:\\Users\\Ishola Francis Ayinde\\Python files\\blind-traffic-light-pedestrian-crossing-sounds.mp3')

def turn_off_red_light():
  draw_circle(15, 15, 30, "grey", "black")

def turn_off_white_light():
  draw_circle(15, -75, 30, "grey", "black")

# This variable holds the current state of the machine
light_box_state = ""

# Set timers for the light durations
window.ontimer(lambda: draw_circle(15, 15, 30, "black", ""), )
window.ontimer(lambda: draw_circle(15, -75, 30, "black", ""), )

# Call the machine every 1000 milliseconds
def advanced_machine():
  global light_box_state

  draw_circle(15, 15, 30, "black", "")
  draw_circle(15, -75, 30, "black", "")

  if light_box_state == "red":
    play_alarm()

  if light_box_state =="red":
    turn_off_white_light()

  if light_box_state == "white":
    turn_off_red_light()

  # Turn on the light for the white state.
  if light_box_state == "red":
    draw_circle(15, 15, 30, "black", "red")
    draw_circle(15, -75, 30, "black", "")
    time.sleep(15) #Stimulating approximately 150seconds for white light. My Computing limitations to play the sound, draw circles and turn on light concurrently while running the other aspect 
                    #of the algorithm drags the timer for 10 extra seconds. but should be fine on a faster computer with more processing power and memory
    
    light_box_state = "white"

# Turn on the light for the red state.
  else:
    light_box_state == "white"
    draw_circle(15, 15, 30, "black", "")
    draw_circle(15, -75, 30, "black", "white")
    time.sleep(20) #Stimulating approximately 200seconds for red light
    
    light_box_state = "red"

  window.ontimer(advanced_machine, 2000)
advanced_machine()
window.mainloop()
