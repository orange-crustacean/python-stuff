def make_pyramid(rows):

    string = ''

    for i in range(rows + 1):
        row = ''
        for j in range(i):
            row += str(i)
            if j < i - 1:
                row += '.'
        
        length = (len(str(rows)) + 1) * rows
        row = row.center(length)
        string += row + '\n'

    return string

num = int(input('how many rows: '))

pyramid = make_pyramid(num)

print(pyramid)