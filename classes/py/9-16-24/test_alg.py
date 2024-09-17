import timeit


data = ["1", "2", "3", "4", "5"] * 1000

# def test1(data, item):
#     print(data.index(item))


def test1():
    for item in data:
        amount = len(data)
        result = f'{item} / {amount}'
       # print(result)

def test2():
    amount = len(data)

    for item in data:
        result = f'{item} / {amount}'
       # print(result)

print(timeit.timeit(test1, number=100000))
print(timeit.timeit(test2, number=100000))

# test1()
# test2()