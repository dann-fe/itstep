countries = [
    ["cz", 10_800_000],
    ["sk", 6_000_000],
    ["de", 50_000_000]
]

for item in range(0, len(countries)):
    name = countries[item][0]
    population = countries[item][1]
    print(name, population)