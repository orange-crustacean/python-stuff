import turtle

class Face:
    def __init__(self, mouth, mood, eye):
        self.mouth = mouth
        self.mood = mood
        self.eye = eye

moody = Face("smile", "yellow", "black")

def changeMouth():
    if moody.mouth == "smile":
        moody.mouth = "frown"
    elif moody.mouth == "frown":
        moody.mouth = "smile"

def changeMood():
    if moody.mood == "yellow":
        moody.mood = "red"
    elif moody.mood == "red":
        moody.mood = "yellow"

def changeEye():
    if moody.eye == "black":
        moody.eye = "blue"
    elif moody.eye == "blue":
        moody.eye = "black"

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
    playing = True
    while playing:
        turtle.speed(5)
        print("moodys mood is", moody.mood)
        turtle.clear()
        drawFace(moody.mouth, moody.mood, moody.eye)
        while True:
            print("\nChange Moody's Face")
            print("1) Make me ")
            print("2) Make me angry")
            print("3) Make my eyes blue")
            print("4) quit")
            action = input("Enter a selection: ")
            action = int(action) if action.isdigit() else None
            
            if action == 1:
                changeMouth()
            elif action == 2:
                changeMood()
            elif action == 3:
                changeEye()
            elif action == 4:
                playing = False
            else:
                continue
            break
                

    

main()