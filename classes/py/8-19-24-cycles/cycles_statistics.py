
data = [124,21, 214, 543, 298, 109, 72, 978, 198, 1, -147, -25, 12908, -1294, 3948, 197, -120, 120]

biggest_number = data[0]


def min_num (data: list[int]):
    smallest_number = data[0]
    for i in data:
        if i < smallest_number:
            smallest_number = i
            print(f'{smallest_number} is the new smallest number')
        else:
            print(f'{i} is not smaller than {smallest_number}')
    print(smallest_number)

def max_num (data: list[int]):
    biggest_number = data[0]
    for i in data:
        if i > biggest_number:
            biggest_number = i
            print(f'{biggest_number} is the new biggest number')
        else:
            print(f'{i} is not bigger than {biggest_number}')
    print(biggest_number)


max_num(data)

min_num(data)
