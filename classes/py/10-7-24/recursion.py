def test(num):
    print(num)
    if num < 100:
        test(num + 1)
    else:
        print("end")

test(10)