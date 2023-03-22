#this program tells you interesting stuff about your pay rate and that jazz
#get the informatino about the employee or person 
name = input('Enter employee\'s name: ')
hours = input('Enter number of hours worked in a week: ')
pay_rate = input('Enter hourly pay rate: ')
fed_tax = input('Enter federal tax withholding rate (ex. 0.12): ')
state_tax = input('Enter state tax withholding rate (ex. 0.06):')

#define the string that we are going to be adding everything to
string = '\n'

#header formatting
name = name.upper() + ' PAY INFORMATION'
name = name.center(50)

string += name


## PAY ##
#two new lines plus 'pay' centered with the title
string += '\n \n'
string += 'Pay'.center(50)

#new line plus 'hours worked' aligned to the right
string += '\n' + 'Hours worked: '.rjust(33)

#aligning hours worked with right margin
string += hours.rjust(10)

#pay rate
#align this new line with the colon, and then ad the dollar sign afterwards
string += '\n' + 'Pay rate: '.rjust(33) + '$'
string += pay_rate.rjust(9)

#calculate gross pay, then turn it back into a string
gross = str(round(int(hours) * float(pay_rate), 2))

string += '\n' + 'Gross Pay: '.rjust(33) + '$'
string += gross.rjust(9)


## DEDUCTIONS ##

string += '\n \n'
string += 'Deductions'.center(50)

#calculate federal witholding
fed_withold = int(fed_tax) * int(gross)

string += ('Federal Witholding (' + fed_tax + '): ').rjust(33) + '$'
string += str(fed_withold).rjust(9)


print(string)