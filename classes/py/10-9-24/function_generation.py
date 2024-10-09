def create_op(multiply):
    def op(a, b):
        return (a + b) * multiply
    return op


a = create_op(10)

print(a(1, 2))