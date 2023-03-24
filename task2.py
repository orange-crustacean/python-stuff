import turtle


#prompt the user for the specifications of the circle
x = int(input('where should we put the target(x value, center is (0,0): '))
y = int(input('where should we put the target(y value, center is (0,0): '))
diameter = int(input('what should the diameter of the target be: '))

#setting up our turtle 
turtle.shape('turtle')
turtle.color('black')
turtle.speed(5)
turtle.pensize(3)
turtle.penup()

#move to where the circles center is
turtle.goto(x, y)
turtle.setheading(270)
turtle.forward(diameter)

#first circle
turtle.color('black')
turtle.pendown()
turtle.setheading(0)
turtle.begin_fill()
turtle.circle(diameter)
turtle.end_fill()
turtle.setheading(90)
turtle.penup()
turtle.forward(diameter/4)

#second circle
turtle.color('blue')
turtle.pendown()
turtle.setheading(0)
turtle.begin_fill()
turtle.circle(diameter*(3/4))
turtle.end_fill()
turtle.setheading(90)
turtle.penup()
turtle.forward(diameter/4)

#third circle
turtle.color('red')
turtle.pendown()
turtle.setheading(0)
turtle.begin_fill()
turtle.circle(diameter*(2/4))
turtle.end_fill()
turtle.setheading(90)
turtle.penup()
turtle.forward(diameter/4)

#fourth circle
turtle.color('yellow')
turtle.pendown()
turtle.setheading(0)
turtle.begin_fill()
turtle.circle(diameter*(1/4))
turtle.end_fill()
turtle.setheading(90)
turtle.penup()
turtle.forward(diameter/4)

