products = ["Notebook", "Pen", "Bag"]
prices = [80, 20, 900]
quantities = [3, 5, 1]

subtotal = 0
for i in range(len(products)):
    cost = prices[i] * quantities[i]
    subtotal += cost
    print(products[i], ":", cost)

discount = 0
if subtotal >= 1000:
    discount = subtotal * 0.10

total = subtotal - discount
budget = 1500

print("Subtotal:", subtotal)
print("Discount:", discount)
print("Final bill:", total)

if total > budget:
    print("Over budget by:", total - budget)
else:
    print("Within budget. Balance:", budget - total)
