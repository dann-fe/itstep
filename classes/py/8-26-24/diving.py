oxygen = 100
deeper = 1.5
min_oxygen = 50

while oxygen > min_oxygen:
    oxygen = oxygen - deeper
    print(f'current oxygen: {oxygen}')
else:
    print("go back up")

    