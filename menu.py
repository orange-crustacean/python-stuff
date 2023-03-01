import os

cost = 0

#item class
class item_class():
    def __init__(self, name, price, info):
        self.name = name
        self.price = price
        self.info = info

#add the pizzas to the class
chz_pizza = item_class('cheese pizza', 6.99, 'Classic cheese pizza. \nContains: gluten, milk, trace amounts of maple syrup.')
pp_pizza = item_class('pepperoni pizza', 7.99, 'Cheese pizza with pepperoni on top. \nContains: gluten, milk, trace amounts of school lunch meat.')
hw_pizza = item_class('hawaiian pizza', 7.99, 'Bread, sauce, cheese topped with canadian bacon and pineapple. \nContains: gluten, milk, trace amounts of nuclear waste.' )
mrg_pizza = item_class('margherita pizza', 8.99, 'Bread and sauce topped with real mozzeralla cheese and basil leaves. \nContains: gluten, milk, large amounts in inner peace and happines.')

#add the sides to the class
fries = item_class('fries', 2.99, 'Potato sticks deep fried in vegetable oil. \nContains: fries.')
salad = item_class('salad', 3.99, 'Romaninan lettuce with croutons and parmesean sprinkled on top. \nContains: milk, salad.')
onion_rings = item_class('onion rings', 4.99, 'A ring of onion thats been breaded and deep fried in vegetable oil. \nContains: gluten, crunchy glimps of heaven.')

#add the drinks to the class
water = item_class('water', 0.99, 'Plain old water. nothing more to it. \nContains: water, more water.')
pepsi = item_class('pepsi', 1.99, 'Average Pepsi soda. \n Contains: caffeine, large amounts of sugar.')
maple_syrup = item_class('maple syrup', 2.99, 'Sweet maple syrup imported daily from canada. a little taste of home for our foreign friends. \nContains: canadian DNA.')

#list of all the items
catalouge = [chz_pizza, pp_pizza, hw_pizza, mrg_pizza, fries, salad, onion_rings, water, pepsi, maple_syrup]

os.system('cls')
##intro##
print('')
print('')
print('Welcome to Jones Pizzaria, may I take your order?')

print('')
print('Entres:')

#pizza options
print('')
print('Pizzas: ')
print('Cheese Pizza........................................................$6.99')
print('Pepperoni Pizza.....................................................$7.99')
print('Hawaiian Pizza......................................................$7.99')
print('Margherita Pizza....................................................$8.99')

#sides options
print('')
print('Sides:')
print('Fries...............................................................$2.99')
print('Salad...............................................................$3.99')
print('Onion rings.........................................................$4.99')

#drink options
print('')
print('Water...............................................................$0.99')
print('Pepsi...............................................................$1.99')
print('Maple Syrup (for the canadians).....................................$2.99')

#tell the user the avaliable commands to use when ordering
print('')
print('')
print('While ordering, type these comands to complete an action:')
print('')
print('"add": adds an item to your order')
print('"remove": removes an item from your order')
print('"info" tells you information about a specific menu item')
print('"review" tells the user all the items on their current order.')
print('"finish" confirms your order')
print('Type "back" at any time to go back to the initial prompt. ')

order = []
avaliable = True

##loop##
ordering = True
while ordering:
    print('')
    command = input('Please enter the action you would like to complete: ')
    print('')

    #add the item to the order list
    if command == 'add':
        add = input('Enter the item you would like to add (no caps): ')

        if add == 'back':
            continue
        else:
            for i in catalouge:
                if add == i.name:
                    avaliable = True
                    order.append(i)
                    print('Successfully added ' + str(add) + '.')
                    break
                else:
                    avaliable = False

            if not avaliable:
                print('Sorry, we do not produce that item. Please try again.')
    

    #remove the item from the order list
    elif command == 'remove':
        add = input('Enter the item you would like to add (no caps): ')

        if add == 'back':
            continue
        else:
            for i in order:
                if add == i.name:
                    avaliable = True
                    order.remove(i)
                    print('Successfully removed ' + str(add) + '.')
                    break
                else:
                    avaliable = False

            if not avaliable:
                print('That item is not in your order.')
    

    #tell user info about specified item
    elif command == 'info':
        item_info = input('Enter the item you would like more information about: ')

        if item_info == 'back':
            continue
        else:
            for i in catalouge:
                if item_info == i.name:
                    print('')
                    print(i.info)


    #print the users order
    elif command == 'review':
        cost = 0
        print('Your order:')

        for i in order:
            print(i.name)
            cost += i.price
        print('Total cost: $' + str(cost))


    #finish the order
    elif command == 'finish':
        print('Thank you for choosing Jones Pizzaria, enjoy your meal :)')
        ordering = False

    else:
        print("Sorry, I didn't get that. Please try again.")
