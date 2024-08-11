required_age = input("write your required age: ")
required_age = int(required_age)
age = input("write your age: ")
age = int(age)
print("your age is ", age)
print(type(age))

if age < required_age:
    print("your age doesnt match the requirement")

elif age == required_age:
    print("your age is identical to the requirement")
else:
    print("your age matches the requirement")
