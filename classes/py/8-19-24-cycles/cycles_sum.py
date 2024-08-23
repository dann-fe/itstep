data = [124,21, 214, 543, 298, 109, 72, 978, 198, 1, -147, -25, 12908, -1294, 3948, 197, -120, 120]

def data_sum(data: list[sum]):
    result = 0
    for i in data:
      result = result + i  
    return result 

def main():
    data = [124,21, 214, 543, 298, 109, 72, 978, 198, 1, -147, -25, 12908, -1294, 3948, 197, -120, 120]
    result = data_sum(data)
    print(result)

main()