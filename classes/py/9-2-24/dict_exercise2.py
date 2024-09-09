sample_dict = {'a': 100, 'b': 200, 'c': 300}

print(sample_dict.values())

num = int(input("check if a number is in sample_dict: "))


if num in sample_dict.values():
    print(True)
else: 
    print(False)
