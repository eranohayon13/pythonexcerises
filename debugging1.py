user_funds = 10.31
item_price = 5.70

if item_price < user_funds:
    print("You have enough money!")
elif item_price == user_funds:
    print("You have the precise amount of money")
else:
    print("Sorry you don't have enough money")