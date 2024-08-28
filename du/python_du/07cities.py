eu_cities = [
    ['Berlin', 3669491, 891],   #city name, population, area
    ['Madrid', 3223334, 604],
    ['Rome', 2872800, 1285],
    ['Paris', 2165423, 105],
    ['Bucharest', 1883425, 228],
    ['Budapest', 1746344, 525],
    ['Warsaw', 1790658, 517],
    ['Vienna', 1921153, 414],
    ['Hamburg', 1841179, 755],
    ['Barcelona', 1620343, 101]
]



# for value in range(0, len(eu_cities)):
#     print(f'there are {eu_cities[value][1]} people living in {eu_cities[value][0]}')

max_population = 0
max_population_city = ""
for value in range(0, len(eu_cities)):
    if eu_cities[value][1] > max_population:
        max_population = eu_cities[value][1]
        max_population_city = eu_cities[value][0]
print(f"the max_population is {max_population} in {max_population_city}")


total_population = 0
for i in range(0, len(eu_cities)):
    total_population = eu_cities[value][1] + total_population
print(f'the total population is {total_population}')

min_population = 10**10
min_population_city = ""
for value in range(0, len(eu_cities)):
    if eu_cities[value][1] < min_population:
        min_population = eu_cities[value][1]
        min_population_city = eu_cities[value][0]
print(f"the smallest population is {min_population} in {min_population_city}")