from shopping_functions import *

def main():
    shopping = True
    while shopping: 
        print("Avaliable actions: \n  1) Add an item\n  2) Remove an item\n  3) Search for item\n  4) Print final list\n  5) Check out")
        action = input("Which action would you like to perform (1-5): ")
        if action == '1':
            adder()
        elif action == '2':
            remover()
        elif action == '3':
            search()
        elif action == '4':
            printList()
        elif action == '5':
            checkOut()
            shopping = False
        else:
            print("Sorry, I don't think that is a valid action. Please try again.")
        print('')

main()