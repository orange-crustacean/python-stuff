import random            

def main():
    print("I'm thinking of a number between 1 and 100.")
    guesses = 0
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

            with open("C:/users/jskhqzt/python-stuff/num_game/highscores.txt", "r") as f:
                lines = f.readlines()

            with open("C:/users/jskhqzt/python-stuff/num_game/highscores.txt", "w") as f:
                string = "Highscores:"
                for i in range(1, 11):
                    string += ("\n" +  (str(i) + ") ").rjust(5) +  lines[i[5:6]])

                f.write(string)

            with open("C:/users/jskhqzt/python-stuff/num_game/highscores.txt", "r") as f:
                print("\n" + f.read())


            guessing = False
        print("")

main()