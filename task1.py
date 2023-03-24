#prompt user for these 4 variables
investment_amount = float(input('what is your investment amount? '))
monthly_payment_amount = float(input('what is your monthy payment amount? '))
annual_interest_rate = float(input('what is your annual interest rate? enter as a percentage, but without the % sign '))
num_years = int(input('how many years: '))

#convert the months into years
monthly_interest_rate = annual_interest_rate /12 /100
num_months = num_years * 12

#the equation is  broken into left and right chunks because it is big
#left half calculations
left = (investment_amount * (1 + monthly_interest_rate)**num_months)

#right half calculations
right = monthly_payment_amount * ((((1 + monthly_interest_rate)**num_months) - 1)/monthly_interest_rate) * (1 + monthly_interest_rate)

#finish the calculations and round to 2 decimal places
future_value = round((left + right), 2)

#print the future value
print('Your future value is $' + str(future_value))