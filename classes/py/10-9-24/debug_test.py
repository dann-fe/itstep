from decorator import test1 # type: ignore

def main():
    result = test1()

    for item in ["A", "B", "C"]:
        print(item)

main()