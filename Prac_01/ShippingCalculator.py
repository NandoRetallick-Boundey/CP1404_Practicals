
total = 0

shipping_items = int(input("Number of Items: "))

while shipping_items <= 0:
    print("Invalid number of Items")
    items = int(input("Number of Items: "))

for i in range(0, shipping_items):
    Price = float(input("Price of Item: $"))
    total += Price

if total > 100:
    total *= 0.9

print("Total price for {} Items is ${}".format(shipping_items, total))
