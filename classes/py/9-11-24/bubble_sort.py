nums = [86, 28, 8, 1, 6, 17, 25, 50, -12]

def bubble_sort(data):

    for a in range(len(data) - 1):
        for i in range(0, len(nums) - 1):
            x = i
            y = i + 1

            a = data[x]
            b = data[y]
            print(a, b, i, i + 1)

            if a > b:
                data[x] = b
                data[y] = a
        
        print(nums)


bubble_sort(nums)