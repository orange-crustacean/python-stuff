string = ''

rows = 20

for i in range(rows):
    row = ''
    for j in range(i):
        row += str(i) + ' '
    
    length = (len(str(rows)) + 1) * rows
    row = row.center(length)
    string += row + '\n'

print(string)