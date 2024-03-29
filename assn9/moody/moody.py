import turtle
from moody_class import Face

moody = Face("smile", "yellow", "black")

def getOpposite(thingy):
    if thingy == "mouth":
        if moody.mouth == "smile":
            return "frown"
        else:
            return "smile"
    elif thingy == "mood":
        if moody.mood == "yellow":
            return "angry"
        elif moody.mood == "red":
            return "happy"
    elif thingy == "eye":
        if moody.eye == "black":
            return "blue"
        else:
            return "black"

def drawSmile():
    turtle.setheading(210)
    for i in range(1, 50):
        turtle.forward(2)
        turtle.right(1.2)

def drawFrown():
    turtle.setheading(150)
    for i in range(1, 50):
        turtle.forward(2)
        turtle.left(1.2)

def drawFace(mouth, mood, eye):
    turtle.color("black", mood)

    #draw head
    turtle.penup()
    turtle.goto(0,-100)
    turtle.setheading(0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(150)
    turtle.end_fill()

    #draw eyes
    turtle.color("black", eye)
    turtle.penup()
    turtle.goto(-50, 70)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(10)
    turtle.penup()
    turtle.goto(50, 70)
    turtle.pendown()
    turtle.circle(10)
    turtle.end_fill()

    #draw mouth
    turtle.penup()
    turtle.goto(50, -50)
    turtle.pendown()

    drawSmile() if mouth == "smile" else drawFrown()

    turtle.penup()
    turtle.goto(0,0)

def main():
    turtle.speed(10)
    turtle.width(3)
    playing = True
    while playing:
        turtle.clear()
        drawFace(moody.mouth, moody.mood, moody.eye)
        while True:
            print("\nChange Moody's Face")
            print("1) Make me " + getOpposite("mouth"))
            print("2) Make me " + getOpposite("mood"))
            print("3) Make my eyes " + getOpposite("eye"))
            print("4) quit")
            action = input("Enter a selection: ")
            action = int(action) if action.isdigit() else None
            
            if action == 1:
                moody.changeMouth()
            elif action == 2:
                moody.changeMood()
            elif action == 3:
                moody.changeEye()
            elif action == 4:
                playing = False
            else:
                continue
            break
                

    

main()