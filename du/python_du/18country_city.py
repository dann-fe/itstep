"""
Stat
Mesto

oba budou mít název, mesto bude mít referenci na stát
Mesto tedy na venek dokáže zjistit název státu ke kterému patří
Mesto bude mít metodu info, která vypíše:
- "Město ABC leží ve státě XYZ"

Bonusový úkol:
Stat bude mít metodu info, která dokáže zjistit, kolik má měst
- implementaci nechám na vás

použití:

dansko = Stat('Dansko')
norsko = Stat('Norsko')

kodan = Mesto('Kodaň', dansko)
hovedstaden = Mesto('Hovedstaden', dansko)

oslo = Mesto('Oslo', norsko)

oslo.info() # vypíše "Město Oslo leží ve státě Norsko"
kodan.info() # vypíše "Město Kodan leží ve státě Dánsko"
"""

class City:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __repr__(self):
        return self.name
    
    def info(self):
        return f"{self.name} is located in {self.country}"

class Country:
    def __init__(self, name: str):
        self.name = name
        self.cities = []
    
    def add_city(self, city: str):
        self.cities.append(city)
        city.country = self
    
    def __repr__(self) -> str:
        return self.name

    def return_cities(self):
        return self.cities
    
    def city_amount(self):
        return f"there are {self.cities.__len__()} cities in {self.name}"

usa = Country("USA")
japan = Country("Japan")
uk = Country("United Kingdom")

london = City("London", uk)
birmingham = City("Birmingham", uk)
manchester = City("Manchester", uk)
bristol = City("Bristol", uk)
newcastle = City("Newcaslte", uk)
oxford = City("Oxford", uk)

uk.add_city(london)
uk.add_city(birmingham)
uk.add_city(manchester)
uk.add_city(bristol)
uk.add_city(newcastle)
uk.add_city(oxford)

print(uk.city_amount())
