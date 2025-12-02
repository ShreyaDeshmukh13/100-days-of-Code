from turtle import Turtle ,Screen
import turtle
import random

t = Turtle()
screen = Screen()
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colors = (r,g,b)
    return colors

t.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        t.circle(100)
        t.color(random_color())
        current_heading = t.heading()
        t.setheading(current_heading + 10)


draw_spirograph(5)
screen.exitonclick()