import random

simulating = True

while simulating:

    #reset variables
    found_1 = 0
    found_2 = 0
    found_some = 0

    nights = int(input('How many nights should the simulation run: '))

    #get which cell each one goes to
    for i in range(nights):
        el1 = random.randint(1, 6)
        el2 = random.randint(1, 6)
        zoo_dude = random.randint(1, 6)

        #checks if the zookeeper checks same cell as the elephants
        if zoo_dude == el1 or zoo_dude == el2:
            found_1 += 1

            #tracking the nights that any were found to find the second statistic
            found_some += 1

            #checks if the cell he checks has both elephants in it
            if zoo_dude == el1 and zoo_dude == el2:
                found_2 += 1

    #calculations
    percent_1 = round(found_1 / nights, 2)
    percent_2 = round(found_2 / found_some, 2)

    #which one is correct
    if percent_1 == 0.33 and percent_2 == 0.16:
        truth = 'Zookeeper was correct.'
    else:
        truth = 'Custodian was correct.'
        

    print('Percent that at least 1 elephant was found: ' + str(percent_1))
    print('Percent that of the times an elephant was found, both were in there: ' + str(percent_2))

    print(truth)

    query = input('\nWould You like to run the simulation again (y/n): ')

    if query == 'y':
        continue
    else:
        break