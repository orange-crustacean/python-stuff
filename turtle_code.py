import turtle
import time

#screen
width = 700
height = 650
turtle.screensize(width, height)

#seting up our turtle boy
tim = turtle.Turtle()
tim.color('black', 'white')
tim.shape('turtle')
tim.pensize(3)
tim.speed(7)

tim.penup()

#begin drawing the three circles to make snowman body
tim.setheading(270)
tim.forward(350)
tim.setheading(0)

tim.pendown()
tim.begin_fill()
tim.circle(150)
tim.end_fill()
tim.penup()

tim.setheading(90)
tim.forward(250)
tim.setheading(0)

tim.pendown()
tim.begin_fill()
tim.circle(100)
tim.end_fill()
tim.penup()

tim.setheading(90)
tim.forward(166)
tim.setheading(0)

tim.pendown()
tim.begin_fill()
tim.circle(50)
tim.end_fill()
tim.penup()

#setting tim up to make the buttons
tim.pensize(10)

tim.setheading(270)
tim.forward(350)
tim.setheading(90)

tim.pencolor('green')

for i in range(3):
    tim.pendown()
    tim.dot(20)
    tim.penup()
    tim.forward(70)

tim.forward(40)

for i in range(3):
    tim.pendown()
    tim.dot(15)
    tim.penup()
    tim.forward(30)

tim.setheading(210)
tim.forward(100)


#left arm
tim.pensize(10)
tim.color('brown')

tim.setheading(160)
tim.pendown()
tim.forward(150)

tim.left(40)
tim.forward(30)
tim.left(180)
tim.forward(30)

tim.left(140)
tim.forward(30)
tim.right(180)
tim.forward(30)

tim.left(140)
tim.forward(30)
tim.left(180)
tim.forward(30)

#move to other side of body
tim.penup()
tim.setheading(340)
tim.forward(175)
tim.setheading(0)
tim.forward(150)
tim.pendown()


#right arm
tim.setheading(20)
tim.pendown()
tim.forward(150)

tim.right(40)
tim.forward(30)
tim.right(180)
tim.forward(30)

tim.right(140)
tim.forward(30)
tim.right(180)
tim.forward(30)

tim.right(140)
tim.forward(30)
tim.right(180)
tim.forward(30)

#move tim back to center
tim.penup()
tim.setheading(200)
tim.forward(175)
tim.setheading(180)
tim.forward(63)
tim.setheading(90)

tim.forward(125)
tim.setheading(0)

#eyes
tim.color('black')
tim.forward(25)
tim.dot(20)

tim.setheading(180)
tim.forward(50)
tim.dot(20)

#back to center of head
tim.setheading(0)
tim.forward(25)

#mouth
tim.setheading(270)
tim.forward(25)
tim.color('purple')
tim.pensize(3)
tim.pendown()

tim.setheading(0)
tim.forward(15)
tim.setheading(180)
tim.forward(30)
tim.penup()

#move to top of head
tim.setheading(0)
tim.forward(15)
tim.setheading(90)
tim.forward(60)

#hat
tim.color('pink', 'orange')
tim.pensize(5)
tim.begin_fill()
tim.pendown()

#bottom of hat
tim.setheading(0)
tim.forward(50)


#bottom right side
tim.setheading(90)
tim.forward(15)

#top right side
tim.setheading(180)
tim.forward(30)

#middle right side
tim.setheading(90)
tim.forward(30)

#middle top
tim.setheading(180)
tim.forward(40)

#middle left side
tim.setheading(270)
tim.forward(30)

#top left side
tim.setheading(180)
tim.forward(30)

#bottom left side
tim.setheading(270)
tim.forward(15)

#bottom
tim.setheading(0)
tim.forward(50)

tim.penup()
tim.end_fill()

time.sleep(5)








