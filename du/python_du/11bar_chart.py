import matplotlib.pyplot as plt

data = {
    'Praha': 1_384_732,
    'Brno': 400_566,
    'Ostrava': 284_765,
    'Plzen': 185_599,
}

plt.figure(figsize=(8, 5))
plt.bar(data.keys(), data.values(), color='navy')
plt.ticklabel_format(style='plain', axis='y')
plt.title("Population in czech cities (in millions)")
plt.xlabel("City")
plt.ylabel("Population")
plt.show()