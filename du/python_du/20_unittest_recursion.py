import unittest as ut

def factorial_loop(n):
    result = 1
    while n > 1:
        result = result * n
        n = n - 1
    
    return result

class FactorialTest(ut.TestCase):
    def test_factorial0(self):
        result = factorial_loop(0)
        self.assertEqual(result, 1)

    def test_factorial1(self):
        result = factorial_loop(1)
        self.assertEqual(result, 1)

    def test_factorial5(self):
        result = factorial_loop(5)
        self.assertEqual(result, 120)        

ut.main()

def calculate(a, b, callback):
    return callback(a, b)


def add(a, b):
    return a + b

def sub(a, b):
    return a - b

print(calculate(7, 3, add))