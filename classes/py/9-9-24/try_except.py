try:
    print(1)
    print(3/ 0)
    print(2)

except ZeroDivisionError:
    print(0)
except Exception as e:
    print(type(e))
finally:
    print("this part always occurs")