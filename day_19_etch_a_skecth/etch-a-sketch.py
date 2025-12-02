from turtle import Turtle , Screen

t = Turtle()
screen = Screen()


def moveforwards():
    t.forward(10)

def movebackwards():
    t.backward(10)

def turn_left():
    new_heading = t.heading() + 10
    t.setheading(new_heading)

def turn_right():
    new_heading = t.heading() - 10
    t.setheading(new_heading)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen.listen()
screen.onkey(key = "w" ,fun = moveforwards)
screen.onkey(key = "s" , fun = movebackwards)
screen.onkey(key = "a" , fun = turn_left)
screen.onkey(key = "d" , fun = turn_right)
screen.onkey(key="c",fun=clear)

screen.exitonclick()