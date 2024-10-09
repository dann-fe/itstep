"""
!4 = 1.2.3.4 = !3.4

!n = !(n - 1) * n

"""

def factorial(n: int):
    if n == 2:
        return 2
    if n < 2:
        return 1
    if n < 0:
        raise ValueError
    result = factorial(n - 1) * n
    return result

def factorial_loop(n):
    result = 1
    while n > 1:
        result = result * n
        n = n - 1
    
    return result


print(factorial(5))
print(factorial_loop(5))


def test_recursion():
    factorial(100)

def test_loop():
    factorial_loop(100)

import timeit
print(timeit.timeit(test_recursion, number = 100000))
print(timeit.timeit(test_loop, number = 100000))