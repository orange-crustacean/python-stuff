#we will be calculating the area of a regular polygon
import math
from math import pi

print('Welcome to calculating area of regular polygon, yayyy!!')

#ask user for the number of sides (shape) and the length of each side
sides = int(input('how many sides does this lovley polygon have: '))
length = float(input('how long is each side: '))

#calculate (broken into 2 sections for simplicity)
top = sides*math.pow(length, 2)
bottom = 4*math.tan(pi/sides)

#finish calculations and round
area = round(top/bottom, 5)

print('area of your polygon is ' + str(area))
