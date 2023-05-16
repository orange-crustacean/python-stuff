from blobber import Blobber

def main():
    name = input("Enter your Blobber's name: ").capitalize()
    color = input("Enter your Blobber's color: ").lower()
    radius = eval(input("Enter your Blobber's radius: "))
    height = eval(input("Enter your Blobber's height: "))
    vol = radius * radius * height * 3.14

    myBlobber = Blobber(radius, height, color, name, vol)

    done = False
    time = myBlobber.timer()
    incrementer = myBlobber.increment()

    while not done:
        print()
        print("Main Menu")
        print("\t(1) Display Name")
        print("\t(2) Change Name")
        print("\t(3) Display Color")
        print("\t(4) Change Color")
        print("\t(5) Feed Blobber")
        print("\t(6) Blobber Speak")
        print("\t(7) Exit")

        # Display current vitals and check to see if it has turned to dust
        # This will catch cases where the Blobber was fed too much as well

        vitals, blobberOK = myBlobber.vitalsOK(time, incrementer)
        time = myBlobber.timer()
        print("Your Blobber is at " + format(vitals, ".2%") + " happiness")
        if not blobberOK:
            print("Your Blobber turned to dust")
            break

        choice = eval(input("Make a selection: "))

        # Check to see if the Blobber turned to dust while waiting for the user to make a selection
        vitals, blobberOK = myBlobber.vitalsOK(time, incrementer)
        time = myBlobber.timer()
        if not blobberOK:
            print("Your Blobber is at " + format(vitals, ".2%") + " happiness")
            print("Your Blobber turned to dust")
            break
        
        print()
        if choice == 1:
            displayName(myBlobber)
        elif choice == 2:
            changeName(myBlobber)
        elif choice == 3:
            displayColor(myBlobber)
        elif choice == 4:
            changeColor(myBlobber)
        elif choice == 5:
            feedBlobber(myBlobber)
        elif choice == 6:
            blobberSpeak(myBlobber, vitals)
        elif choice == 7:
            done = True

    print("Thanks for taking care of a Blobber")

def displayName(blobber):
    print("Your Blobber's name is " + blobber.getName())

def changeName(blobber):
    name = input("Enter Blobber's new name: ").capitalize()
    blobber.setName(name)
    displayName(blobber)

def displayColor(blobber):
    print("Your Blobber's color is " + blobber.getColor())

def changeColor(blobber):
    color = input("Enter Blobber's new color: ").lower()
    blobber.setColor(color)
    displayColor(blobber)

def feedBlobber(blobber):
    food = eval(input("Enter amount to you feed your Blobber: "))
    blobber.feedBlobber(food)

def blobberSpeak(blobber, vitals):
    print(blobber.blobberSpeak(vitals))

main()