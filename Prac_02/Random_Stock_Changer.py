import random

MAX_INCREASE = 0.175
MAX_DECREASE = 0.05
MIN_PRICE = 1
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0

day_counter = 0
price = INITIAL_PRICE
print("Starting price: ${:,.2f}".format(price))

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)

    day_counter += 1
    price *= (1 + price_change)
    print("On day {} price is: ${:,.2f}".format(day_counter, price))
