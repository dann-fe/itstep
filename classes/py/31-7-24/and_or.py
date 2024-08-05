cost_limit = 100_000
color = "red"

your_cost = input("your cost is: ")
your_cost = int(your_cost)

your_color = input("your color is: ")

if your_cost <= cost_limit and your_color == color:
    print("the car meets all the requirements")
else:
    print("the car does not meet all the requirements")
