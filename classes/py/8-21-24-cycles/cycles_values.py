prices = [
    "shoes", 1000,
    "dress", 2000,
    "socks", 50,
    "tshirt", 700
]

# for item in range(0, len(prices), 2):
#     print(prices[item])

max_cost = 0
for price in range(0, len(prices), 2):
        # print(prices[price])
    if prices[price + 1] > max_cost:
        max_cost = prices[price + 1]
    print(max_cost)

for item_price in range(0, len(prices), 2):
    print(item_price + 1, prices[item_price], prices[item_price + 1])


