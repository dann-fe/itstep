staty = {
    'CZ': 'Česko',
    'SK': 'Slovensko',
    'PL': 'Polsko',
    'DE': 'Německo',
    'AT': 'Rakousko',
}

staty["HU"] = "Madarsko"
print(staty['AT'])

staty_length = {}   

for country in staty:
    staty_length[country] = len(staty[country])

print(staty_length)