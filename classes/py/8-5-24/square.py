side_lenght = int(input("how long is the side of your square in cms? "))

if side_lenght > 0:
    print("the whole lenght of your square is ", side_lenght * 4, "cm")
    print("the area of your square is ", side_lenght ** 2, "cm²")
else:
    side_lenght = int(input("invalid value, put in a number greater than zero "))
    print("the whole lenght of your square is ", side_lenght * 4, "cm")
    print("the area of your square is ", side_lenght ** 2, "cm²")
