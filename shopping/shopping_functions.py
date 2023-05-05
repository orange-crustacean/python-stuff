groceries = []
clothes = []
electronics = []
books = []
categories = [groceries, clothes, electronics, books]

def sort():
    global groceries
    global clothes
    global electronics
    global books

    groceries = sorted(groceries)
    clothes = sorted(clothes)
    electronics = sorted(electronics)
    books = sorted(books)

def list2string(list):
    string = ""
    for i in list:
        string += i
        if list.index(i) < len(list) - 1:
            string += ', '
    
    return string

def adder():
    while True:
        print("\nAvaliable categories:\n  1) groceries\n  2) clothes\n  3) electronics\n  4) books\n  If you are done, type 'done': ")
        category = input("What category would you like to add an item to (1-4): ")
        if category == 'done':
            break
        elif category.isdigit():
            category = int(category) - 1
            if category <= 3 and category >= 0:
                lst = list2string(categories[category])
                print("\nItems: " + lst)
                item = input("What item would you like to add: ").strip()
                categories[category].append(item)  
        else:
            print("Sorry, I didn't get that. Try again.")
                            

def remover():
    removing = True
    while removing:
        print("\nAvaliable categories:\n  1) groceries\n  2) clothes\n  3) electronics\n  4) books\n  If you are done, type 'done': ")
        category = input("What category would you like to remove an item from (1-4): ")
        if category == 'done':
            break
        elif category.isdigit():
            category = int(category) - 1
            if category <= 3 and category >= 0:
                lst = list2string(categories[category])
                print("\nItems: " + lst)
                item = input("What is the item you would like to remove(hit enter to go back): ")
                for i in categories[category]:
                    if i == item:
                        categories[category].remove(item)
                        return
                print("Sorry, I don't think that item exists. Please try again.")
            else:
                print("Please choose a valid category.")

def search():
    sort()
    while True:
        print("\nAvaliable categories:\n  1) groceries\n  2) clothes\n  3) electronics\n  4) books\n  If you are done, type 'done': ")
        category = input("What category is the item you would like to find(1-4): ")
        if category == 'done':
            break
        elif category.isdigit():
            category = int(category) - 1
            if category <= 3 and category >= 0:
                item = input("What item would you like to find: ")
                for i in categories[category]:
                        if item == i:
                            print("\nYour item is in slot " + str(categories[category].index(i) + 1) + " from the left.")
                            return
        print("Please choose a valid category")

def printList():
    sort()
    gstr = list2string(groceries)
    cstr = list2string(clothes)
    estr = list2string(electronics)
    bstr = list2string(books)

    print("\n  Groceries:     " + gstr)
    print("    Clothes:      " + cstr)
    print("Electronics:      " + estr)
    print("      Books:      " + bstr)

def checkOut():
    print("\nThank you for shopping at That One Store. We hope to see you again!")