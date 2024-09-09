import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 40, 23, 29, 1000]

plt.figure(figsize=(8, 5))

plt.plot(x, y, marker = "x", linestyle = "-", color = "b")
plt.title("cost of gold")
plt.xlabel("day")
plt.ylabel("cost")
plt.show()