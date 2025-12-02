import turtle
from turtle import Turtle ,Screen
import random

t = Turtle()
turtle.colormode(255)
"""colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown",
    "black", "white", "cyan", "magenta", "gold", "navy", "coral", "violet",
    "teal", "chocolate", "turquoise", "plum", "salmon", "indigo", "gray"]"""

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colors = (r,g,b)
    return colors

directions = [0,90,180,270]
t.pensize(5)
t.speed(50)



for _ in range(200):
    #t.color(random.choice(colors))
    t.color(random_color())
    t.forward(30)
    t.setheading(random.choice(directions))
