mesta_cr = {
    "Praha": 1300000,
    "Brno": 380000,
    "Ostrava": 290000,
    "Plzeň": 170000,
    "Liberec": 100000,
    "Olomouc": 100000,
    "Ústí nad Labem": 92000,
    "Hradec Králové": 93000,
    "České Budějovice": 94000,
    "Pardubice": 90000
}


def info(name):
    print(f'{name}, population is {mesta_cr[name]}')


city_name = str(input("Input a big czech city: "))
try:
    
    if city_name not in mesta_cr:
        raise KeyError("The city is not in the dictionary")
    info(city_name)

except KeyError as error:
    print(error)
