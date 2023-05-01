groceries = []
clothes = []
electronics = []
books = []
catagories = [groceries, clothes, electronics, books]

def adder():
    while True:
        print("\nAvaliable catagories:\n  1) groceries\n  2) clothes\n  3) electronics\n  4) books\n  If you are done, type 'done': ")
        catagory = input("What catagory would you like to add an item to (1-4): ")
        if catagory == 'done':
            break
        else:
            catagory = int(catagory) - 1
            print(catagories[catagory])
            item = input("What item would you like to add: ")
            catagories[catagory].append(item)                  

def remover():
    removing = True
    while removing:
        print("\nAvaliable catagories:\n  1) groceries\n  2) clothes\n  3) electronics\n  4) books\n  If you are done, type 'done': ")
        catagory = input("What catagory would you like to remove an item from (1-4): ")
        if catagory == 'done':
            break
        else:
            catagory = int(catagory) - 1
            print(catagories[catagory])
            item = input("What is the item you would like to remove: ")
            for i in catagories[catagory]:
                if i == item:
                    catagories[catagory].remove(item)
                    return
            print("Sorry, I don't think there is an item there. Please try again.")

def search():
    item = input("\nWhat item would you like to find: ")
    for i in catagories:
        for j in i:
            if item == j:
                return i.index(j)

def list2string(list):
    string = ""
    for i in list:
        string += i
        if list.index(i) < len(list) - 1:
            string += ', '
    
    return string

def printList():
    gstr = list2string(groceries)
    cstr = list2string(clothes)
    estr = list2string(electronics)
    bstr = list2string(books)
    large = max(len(gstr), len(cstr), len(estr), len(bstr))

    print("  Groceries: ", end='')
    print(gstr.rjust(large + 5))
    print("    Clothes: ", end='')
    print(cstr.rjust(large + 5))
    print("Electronics: ", end='')
    print(estr.rjust(large + 5))
    print("      Books: ", end='')
    print(bstr.rjust(large + 5))

def checkOut():
    print("Thank you for shopping at That One Store. We hope to see you again!")

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