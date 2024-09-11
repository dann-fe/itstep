def count(a, b, c):
    assert a > 0, "a must be greater than 0"

    if b == 0:
        raise ValueError("b cant be 0")

    return a / b * c


try:
    print(count(4, 3, 2))
    print(count(2, 0, 3))
    print(count(2, 3, 4))
except NameError as ne:
    print(f'error, {ne}')

except AssertionError as err:
    print(err)

except ValueError as err:
    print(err)
except:
    print("unknown error")
