import matplotlib.pyplot as plt

values = [40, 60]
colors = ["red", "blue"]
descriptions = ["mature", "underage"]

plt.figure(figsize=(8, 8))

plt.pie(values, label = descriptions, colors = colors, startangle= 0)

plt.show()