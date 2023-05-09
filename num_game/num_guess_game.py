import random            

def main():

    makef = open("C:/users/jskhqzt/python-stuff/num_game/highscores.txt", "a")
    with open("C:/users/jskhqzt/python-stuff/num_game/highscores.txt", "r") as readf:
        lines = readf.readlines()
        for i in range(0, len(lines)):
            lines[i] = int(lines[i])
    writef = open("C:/users/jskhqzt/python-stuff/num_game/highscores.txt", "w")
        
    print("I'm thinking of a number between 1 and 100.")
    guesses = 1
    guessing = True
    num = random.randint(1,100)
    while guessing:
        guess = input("Enter your guess: ")

        try:
            guess = int(guess)
        except:
            ValueError
            print("Thats not an integer. try again.")
            continue

        if guess > num:
            print("Too high, try again.")
            guesses += 1
        elif guess < num:
            print("Too low, try again.")
            guesses += 1
        elif guess == num:
            print("Good job! You guessed correctly.")
            print("It took you", str(guesses), "attempts to correctly guess the number.")
           
            lines.append(guesses)
            lines.sort()
            if len(lines) > 10:
                del lines[:-1]

            string = ""
            for i in range(0, len(lines)):
                string += str(lines[i])
                if i < len(lines) - 1:
                    string += "\n"
                    
            print("\nHighscores:")
            print(string)
            writef.write(string)

            makef.close()
            writef.close()
            guessing = False
        print("")

main()