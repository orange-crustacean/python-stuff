#Jimmy craner
#3rd hour
#mr andrus
#personal space thingymabob

import math

msg = ''
p1_intruding = False
p2_intruding = False

#person 1 info
print('Person 1: ')
p1_name = input('   Enter your name: ')
p1_x = int(input('   Enter your location (x coord): '))
p1_y = int(input('   Enter your location (y coord): '))
p1_radius = int(input('  Enter your personal space radius: '))

#person 2 info
print('Person 2: ')
p2_name = input('   Enter your name: ')
p2_x = int(input('   Enter your location (x coord): '))
p2_y = int(input('   Enter your location (y coord): '))
p2_radius = int(input(' Enter your personal space radius: '))

#calculations
x_dist = abs(p1_x - p2_x)
y_dist = abs(p1_y - p2_y)

dist = math.sqrt(x_dist**2 + y_dist**2)

#test if p1 is intruding
if dist < p1_radius:
    p1_intruding = True

#test if p2 is intruding
if dist < p2_radius:
    p2_intruding = True

#see who is in eachothers personal space
#could be one, the other, both, or neither
if p1_intruding and not p2_intruding:
    msg += p2_name + ' is inside ' + p1_name + '\'s personal space. Please take a step back ' + p2_name + '.'
elif p2_intruding and not p1_intruding:
    msg += p1_name + ' is inside ' + p2_name + '\'s personal space. Please take a step back ' + p1_name + '.'
elif p1_intruding and p2_intruding:
    msg += 'No one is comfortable with how close you to are right now. Both of you need to take a step back please.'
else:
    msg += 'No one is in eachothers personal space. Good job guys, keep up the good work.'

print(msg)
