data = [124,21, 214, 543, 298, 109, 72, 978, 198, 1, -147, -25, 12908, -1294, 3948, 197, -120, 120]

def filter (data = list[int]):
    small_numbers = []

    for i in data:
        if i < 100:
            print(i)
            small_numbers.append(i)
    print(small_numbers)
filter(data)
