def test(*args):
    print(args)

test(1, 2, 3, 4, 5)

def test2(**kwargs):
    a = kwargs["a"]
    b = kwargs["b"]

    print(a + b)

test2(a = 10, b = 20, c = 30)