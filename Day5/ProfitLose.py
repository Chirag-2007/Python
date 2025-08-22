cost_price = int(input("Enter cost price:"))
selling_price = int(input("Enter selling price:"))

if cost_price < selling_price:
    profit = selling_price - cost_price
    print("we have made profit of:", profit)
elif cost_price > selling_price:
    loss = cost_price - selling_price
    print("we have incurred loss of:", loss)
else:
    print("No profit no loss")