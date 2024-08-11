numbers = input("write any amount of numbers you want divided with a blank space: ")

numbers = numbers.split()

numbers = list(map(int, numbers))

print(max(numbers))
print(min(numbers))
print(sum(numbers))

print(sum(numbers) / len(numbers)) # mean
