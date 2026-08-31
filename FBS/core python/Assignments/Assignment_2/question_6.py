# WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic, hra=15% of basic.

basic = int(input('Enter employee basic salary :  '))

da = basic * (10 / 100)
ta = basic * (12 / 100)
hra = basic * (15 / 100)

Total_salary = basic + da + ta + hra
print(f'Total salary of employee is : {Total_salary}')