#jimmy craner
#3rd hour
#mr andrus (it says to provide these in the rubric)
#number guessing game

#imports
import random
num = random.randint(1, 10)
msg = ''

#intro
print('Welcome to the Guessing Game.')
print('The computer has generated a random number 1 through 10. Try to match it.')

guess = int(input('Enter your guess: '))

dist = abs(guess - num)

msg += 'You picked ' + str(guess) + ' while the actual number was ' + str(num) + '.' + '\n'

if dist == 0:
    msg += 'Hmm. Not off by even a little bit. A bit suspicious, no?'
elif dist == 1:
    msg += 'You are a worthy opponent, Knight.'
elif dist == 2:
    msg += 'You have much to learn, Padawan.'
elif dist == 3:
    msg += 'Youngling, your time will come.'
else:
    msg += 'Keep working hard in the Service Corps'

print(msg)