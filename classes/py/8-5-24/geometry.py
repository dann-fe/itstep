values = input("write the lenghts of each side of a triangle in the format 'a b c': ")
print(values.split(" "))

array_values = values.split(" ")
a,b,c = array_values

# print("the total lenght of all sides of your triangle is ", int(array_values[0]) + int(array_values[1]) + int(array_values[2]))

# print("the total lenght of all sides of your triangle is ", int(a) + int(b) + int(c))


print(list(map(int, array_values)))