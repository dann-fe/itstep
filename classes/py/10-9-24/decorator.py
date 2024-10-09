from functools import lru_cache

@lru_cache
def test1():
    print(1)

@lru_cache
def test2():
    print(2)

if __name__ == "__main__":
    #this part of code will run only if this code will be ran in this file
    #if this file is imported, this part of code will not run in the different file
    test1()
    test1()
    test2()
    test2()