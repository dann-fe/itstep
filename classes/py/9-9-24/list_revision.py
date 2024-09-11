# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# print(list1[2][1][2])

# list1[2][1][2].extend(["h", "i", "j"])
# print(list1)


list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

print(list1[2][1][2])

list1[2].extend(["h", "i", "j"])
print(list1)