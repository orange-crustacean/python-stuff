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

#calculate gross pay
gross = float(hours) * float(pay_rate)

string += '\n' + 'Gross Pay: '.rjust(33) + '$'
string += str(gross).rjust(9)


## DEDUCTIONS ##

string += '\n \n'
string += 'Deductions'.center(50)

#calculate federal witholding
fed_withold = round(float(fed_tax) * float(gross), 3)

string += '\n' + ('Federal Witholding (' + fed_tax + '): ').rjust(33) + '$'
string += str(fed_withold).rjust(9)

#state whitholding
state_withold = round(float(state_tax) * float(gross), 3)

string += '\n' + ('State Witholding (' + state_tax + '): ').rjust(33) + '$'
string += str(state_withold).rjust(9)

#total deductions
total_takes = round(state_withold + fed_withold, 3)

string += '\n' + 'Total Deductions: '.rjust(33) + '$'
string += str(total_takes).rjust(9)


##NET PAY##
net_pay = round(gross - total_takes, 3)

string += '\n \n' + 'Net Pay: '.rjust(33) + '$'
string += str(net_pay).rjust(9)

print(string)