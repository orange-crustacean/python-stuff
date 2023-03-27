import random

fluky = []

for i in range (1,10000):
    sum = 0
    for j in range(1,i):
        if i % j == 0:
            random.seed()
            num = i/j
            sum += num
    if sum == i:
        fluky.append(sum)

print(fluky)