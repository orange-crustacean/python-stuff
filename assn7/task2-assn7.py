'''
    This is the starter file. Only fill in the areas indicated.
    Do not modify existing code.
    Replace this file header with the normal file header (name, etc)
'''

#### Add Import Statement(s) as needed ####
import turtle
#### End Add Imp

tim = turtle.Turtle()
tim.penup()
tim.shape('classic')
tim.color('purple', 'white')
tim.speed(5)
tim.pensize(3)

def draw_rect(w, h):
    tim.pendown()
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
    tim.penup()


def drawChessboard(startx, starty, width = 250, height = 250):

    #draw outline
    tim.goto(startx, starty)
    tim.pendown()
    draw_rect(width, height)

    square_width = width / 8
    square_height = height / 8

    tim.color('black')
    tim.speed(15)
    tim.pensize(0)
    tim.hideturtle()

    for i in range(1,9):
        m = i % 2
        
        for j in range(4):
            tim.pendown()
            draw_rect(square_width, square_height)

            tim.forward(square_width * 2)
        
        tim.penup()
        tim.goto(startx + square_width * m, starty + square_height * i)



def main():
    #### Add Code to get input from user ####
    startx = int(input('Enter the desired x location of the bottom left of chessboard: '))
    starty = int(input('Enter the desired y location of the bottom left of chessboard: '))
    width = input('Enter the desired width of the chessboard: ')
    height = input('Enter the desired height of the chessboard: ')

    #### End Add Code to get input from user ####

    if width == "" and height == "":
        drawChessboard(startx, starty)
    elif height == "":
        drawChessboard(startx, starty, width=eval(width))
    elif width == "":
        drawChessboard(startx, starty, height=eval(height))
    else:
        drawChessboard(startx, starty, eval(width), eval(height))


main()