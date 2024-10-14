
with open("C:/Users/adamk/Desktop/programovani/step_fullstack/classes/py/10-14-24/test_file3.txt", mode="wb") as file:
    file.write(b'\xc4\x9b')

with open("C:/Users/adamk/Desktop/programovani/step_fullstack/classes/py/10-14-24/test_file3.txt", mode="rb") as file:
    text = file.read()
    print(text)
    for item in text:
        print(item)