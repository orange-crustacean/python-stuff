'''
    This is the starter file. Only fill in the areas indicated.
    Do not modify existing code.
    Replace this file header with the normal file header (name, etc)
'''

#### Add Import Statement(s) as needed ####
import turtle
#### End Add Imp

tim = turtle.Turtle()

def draw_rect(w, h):
    tim.begin_fill()
    tim.setheading(0)
    tim.forward(w)
    tim.left(90)
    tim.forward(h)
    tim.left(90)
    tim.forward(w)
    tim.left(90)
    tim.forward(h)
    tim.end_fill()
    tim.setheading(0)
    tim.forward(w)



def drawChessboard(startx, starty, width = 250, height = 250):
    tim.penup()
    tim.color('blue')
    tim.speed(4)
    tim.goto(startx, starty)

    #draw rectangle
    tim.pendown()
    tim.goto(startx, starty)
    draw_rect(width, height)

    square_width = width / 8
    square_height = height / 8

    tim.color('black')

    for i in range(1,5):
        m = i % 2
        
        for j in range(4):
            tim.pendown()
            draw_rect(square_width, square_height)

            tim.forward(square_width)
        
        tim.penup()
        tim.goto(startx + square_width * m, starty + square_height * i)



def main():
    #### Add Code to get input from user ####
    startx = int(input('Enter the desired x location of the center of chessboard: '))
    starty = int(input('Enter the desired y location of the center of chessboard: '))
    width = int(input('Enter the desired width of the chessboard: '))
    height = int(input('Enter the desired height of the chessboard: '))

    startx -= width / 2
    starty -= height / 2
    #### End Add Code to get input from user ####

    if width == "" and height == "":
        drawChessboard(startx, starty)
    elif height == "":
        drawChessboard(startx, starty, width)
    elif width == "":
        drawChessboard(startx, starty, height)
    else:
        drawChessboard(startx, starty, width, height)


main()