import random

goal_amount = 10_000_000
current_amount = 0

while current_amount <= goal_amount:
    current_amount += random.randint(1, 1_000) * 1000
    print(f"current amount is {current_amount}")