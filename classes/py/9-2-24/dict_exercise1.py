keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# for i in range(len(keys)):
#     key = keys[i]
#     value = values[i]
#     result[key] = value
# print(result)

result = dict(zip(keys, values))

print(result)