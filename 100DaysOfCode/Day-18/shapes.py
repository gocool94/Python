import random
from turtle import Turtle


timmy = Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_function(sides):
    angle  = 360/sides
    for i in range(sides):
        timmy.forward(90)  # Forward turtle by s units
        timmy.left(angle)

for i in range(3,11):
    timmy.color(random.choice(colours))
    draw_function(i)
