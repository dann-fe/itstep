"""
decorator = function that takes a diff function and return its modified version
"""

def print_result(func):
    def inner():
        result = func()
        print(result)
        return result
    return inner


def calculation():
    return 10 + 20

@print_result
def another():
    return 10 * 20

calculation = print_result(calculation)
calculation()