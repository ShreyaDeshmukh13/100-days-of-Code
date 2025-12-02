from turtle import Turtle ,Screen

t = Turtle()
t.shape('turtle')
screen =  Screen()

for _ in range(3):
    t.color('blue')
    t.forward(100)
    t.left(120)

for _ in range(4):
    t.color('red')
    t.forward(100)
    t.left(90)

for _ in range(5):
    t.color('coral3')
    t.forward(100)
    t.left(72)

for _ in range(6):
    t.color('cyan4')
    t.forward(100)
    t.left(60)

for _ in range(7):
    t.color('dark orchid')
    t.forward(100)
    t.left(51.42)

for _ in range(8):
    t.color('DarkSeaGreen2')
    t.forward(100)
    t.left(45)

for _ in range(9):
    t.color('gray10')
    t.forward(100)
    t.left(40)

for _ in range(10):
    t.color('PaleTurquoise3')
    t.forward(100)
    t.left(36)  


screen.exitonclick()

