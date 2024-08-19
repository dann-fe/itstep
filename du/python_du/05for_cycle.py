mountains = [
    8848, # Mount Everest
    8611, # K2
    4808, # Mont Blanc
    5895, # Kilimanjaro
    3776, # Mount Fuji
    5642, # Elbrus
    1603, # Sněžka
    1492, # Praděd
    1323, # Lysá hora
]

for i in mountains:
    if i < 3000:
        print(f'the mountain thats {i} meters tall is small')
    elif i > 3000 and i < 6000:
        print(f'the mountain thats {i} meters tall is medium tall')
    else:
        print(f'the mountain thats {i} meters tall is large')