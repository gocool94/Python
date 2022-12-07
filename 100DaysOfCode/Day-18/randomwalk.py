import random
from turtle import Turtle
import turtle as t

t.colormode(255)

timmy = t.Turtle()
#colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)
directions = [0,90,180,270]
timmy.pensize(15)
timmy.speed("fastest")

for i in range(200):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))