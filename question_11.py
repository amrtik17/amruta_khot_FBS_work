#Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.
age1 = int(input("Enter age of person 1: "))
age2 = int(input("Enter age of person 2: "))
age3 = int(input("Enter age of person 3: "))
age4 = int(input("Enter age of person 4: "))
age5 = int(input("Enter age of person 5: "))

ticket = float(input("Enter ticket amount per person: "))

if age1 < 12:
    amount1 = ticket * 70 / 100
elif age1 > 59:
    amount1 = ticket * 50 / 100
else:
    amount1 = ticket

if age2 < 12:
    amount2 = ticket * 70 / 100
elif age2 > 59:
    amount2 = ticket * 50 / 100
else:
    amount2 = ticket

if age3 < 12:
    amount3 = ticket * 70 / 100
elif age3 > 59:
    amount3 = ticket * 50 / 100
else:
    amount3 = ticket

if age4 < 12:
    amount4 = ticket * 70 / 100
elif age4 > 59:
    amount4 = ticket * 50 / 100
else:
    amount4 = ticket

if age5 < 12:
    amount5 = ticket * 70 / 100
elif age5 > 59:
    amount5 = ticket * 50 / 100
else:
    amount5 = ticket

total = amount1 + amount2 + amount3 + amount4 + amount5

print("Total ticket amount =", total)