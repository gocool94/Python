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
#directions = [0,90,180,270]
#timmy.pensize(15)
timmy.speed("fastest")

def draw_size_of_gap(size_gap):
    for _ in range(int(360/size_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading()+size_gap)

draw_size_of_gap(5)

screen = t.Screen()
screen.exitonclick()