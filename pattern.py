import turtle
from random import choice

def setup():
    global colors
    colors = ["red", "green", "blue"]
    turtle.color("black")
    turtle.speed(50)
    turtle.screensize(1000, 800)
    turtle.penup()

def drawRectangle(width, height):
    for i in range(1, 5):
        if i % 2 == 0:
            turtle.forward(height)
        elif i % 2 == 1:
            turtle.forward(width)

        turtle.left(90)

def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation):
    turtle.goto(centerX, centerY)
    turtle.setheading(0)
    arcs = 360 / count

    for i in range(1, count + 1):
        turtle.color(choice(colors))
        turtle.forward(offset)
        turtle.left(rotation)
        turtle.pendown()
        drawRectangle(width, height)
        turtle.penup()
        turtle.goto(centerX, centerY)
        turtle.setheading(0)
        turtle.left(arcs * i)

def drawCirclePattern(centerX, centerY, offset, radius, count):
    turtle.goto(centerX, centerY)
    turtle.setheading(0)
    arcs = 360 / count

    for i in range(1, count + 1):
        turtle.color(choice(colors))
        turtle.forward(offset)
        turtle.right(90)
        turtle.pendown()
        turtle.circle(radius)
        turtle.penup()
        turtle.goto(centerX, centerY)
        turtle.setheading(0)
        turtle.left(arcs * i)

def drawSuperPattern():
    

setup()
drawRectanglePattern(-200, 100, 50, 100, 50, 20, 30)

drawCirclePattern(200, -100, -50, 75, 30)





