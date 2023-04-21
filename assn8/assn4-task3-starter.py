

#### Add Import Statement(s) as needed ####
import pattern
#### End Add Import Statement(s) ####


def main():
    # Setup pattern
    pattern.setup()

    # Play again loop
    playAgain = True

    while playAgain:
        # Present a menu to the user
        # Let them select mode
        print("Choose a mode")
        print("1) Rectangle Pattern")
        print("2) Circle Pattern")
        print("3) Super Pattern")
        mode = input("Which mode do you want to play? 1, 2 or 3: ")
        if mode.strip():
            mode = eval(mode)
        else:
            continue
        # If they choose 'Rectangle Patterns'
        if mode == 1:
            #### Add Input Statement(s) as needed ####
            centerX = input("X coordinate for center: ")
            centerY = input("Y coordinate for center: ")
            offset = eval(input("Offset: "))
            width = eval(input("Width: "))
            height = eval(input("Height: "))
            count = eval(input("Count: "))
            rotation = eval(input("Rotation: "))
            #### End Add Inputs Statement(s) ####


            # Draw the rectangle pattern
            pattern.drawRectanglePattern(int(centerX), int(centerY), offset, width, height, count, rotation)

        # If they choose 'Circle Patterns'
        elif mode == 2:
            #### Add Input Statement(s) as needed ####
            centerX = input("X coordinate for center: ")
            centerY = input("Y coordinate for center: ")
            offset = eval(input("Offset: "))
            radius = eval(input("Radius: "))
            count = eval(input("Count: "))
            #### End Add Inputs Statement(s) ####

            # Draw the circle pattern
            pattern.drawCirclePattern(int(centerX), int(centerY), offset, radius, count)

        # If they choose 'Super Patterns'
        elif mode == 3:
            #### Add Input Statement(s) as needed ####
            num = input("How many Super Patterns: ")
            #### End Add Inputs Statement(s) ####
            if num == "":
                pattern.drawSuperPattern(1)
            else:
                pattern.drawSuperPattern(eval(num))

        # Play again?
        print("Do you want to play again?")
        print("1) Yes, and keep drawings")
        print("2) Yes, and clear drawings")
        print("3) No, I am all done")
        response = input("Choose 1, 2, or 3: ")
        #### Add Statement(s) to clear drawings and play again ####
        if response.strip():
            response = eval(response)
        elif response == 1:
            continue
        elif response == 2:
            pattern.reset()
            continue
        elif response == 3:
            playAgain = False
        else:
            continue
        #### End Add Inputs Statement(s) ####

    # print a message saying thank you
    print("Thanks for playing!")
    pattern.done()


main()
