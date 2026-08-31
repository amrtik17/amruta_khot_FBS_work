# Write a program to convert days into years, weeks and days.

days = int(input('Enter days: '))

years = days // 365
remain_days = days % 365

week = remain_days // 7
remain_days = remain_days % 7

print (f'years are : {years}')
print (f'weeks are : {week}')
print (f'days are : {remain_days}')