def count(a, b, callback = None):
    result = a + b
    if callback:
        callback(result)
    return result

def func1(result):
    print("good job, the result is", result)

def func2(result):
    print("amazing job, the result is", result)

def print_result(result):
    print(result)

def save_result(result):
    with open("C:/Users/adamk/Desktop/programovani/step_fullstack/classes/py/10-7-24/result.txt", mode="a", encoding="utf-8") as file:
        file.write(str(result) + "\n")

count(1, 20, print_result)
count(4, 12, save_result)