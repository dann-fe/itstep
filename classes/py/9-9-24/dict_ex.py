# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# # Keys to extract
# keys = ["name", "salary"]

# dict_2 = {x: sample_dict[x] for x in keys}

# # for key in keys:
# #     dict_2[key] = sample_dict[key]

# print(dict_2)


sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {
        'name': 'Brad', 
        'salary': 500
        }
}


sample_dict['emp3']["salary"] = 8500

print(sample_dict)