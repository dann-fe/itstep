fce = lambda x: x * 2

print(fce(10))

def test(x, func):
    return func(x)

test(10, lambda x: x * 2)

nums = [10, 92, 298, 11, 291, 221]

result = filter(lambda x: x > 100, nums)
result2 = [x for x in nums if x % 10 == 2]


result3 = map(lambda x: x * 10, nums)
result4 = [x * 10 for x in nums]
print(list(result))
print(result2)