# WAP to calculate selling price of book based on cost price and discount.

cost_price = int(input('Enter cost price of book : '))
discount = int(input(' Enter how much discount you get : '))

Discount = cost_price * (discount / 100)
selling_price = cost_price -Discount

print(f'selling price of book is : {selling_price}')
