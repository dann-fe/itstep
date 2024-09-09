sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

min_key = ""
min_num = 999999999999999999999999999999999999999999999999999999999999999999999999999999999

for value, key in sample_dict.values(), sample_dict.keys():
    if min_num > sample_dict[value]:
        min_num = sample_dict[value]
        min_key = key
print(min_num, min_key)