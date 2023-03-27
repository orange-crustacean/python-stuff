import random

fluky = []

for i in range (1,10000):
    sum = 0
    for j in range(1,i):
        #once j is greater than half of i, factors will start repeating
        if j <= i/2:
            if i % j == 0:
                random.seed(j)
                num = random.randint(1,i)

                sum += num
    if sum == i:
        fluky.append(sum)
    #there are only 7 fluky nums (in range 10000) so we can skip once we have them
    if len(fluky) == 7:
        break

print(fluky)