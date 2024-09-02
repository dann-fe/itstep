text = "sdneiofweoifnweofweofnowefowinfowihwohpjweoweoncqpncqpofjonvopqpjqpwj"

data = {

}

for letter in text:
    if letter not in data:
        data[letter] = text.count(letter)

print(data)