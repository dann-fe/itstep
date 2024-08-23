students = ["dan", "beer", "cecil", "doga", "egundo", "frilip", "gikep", "hynek", "imbecil", "jipif"]

numof_s = len(students)

for test_a in range(0, numof_s, 2):
    print(test_a + 1, students[test_a])

for index in range(0, numof_s, 3):
    if index + 1 < numof_s and index + 2 < numof_s:   
        print(students[index], students[index + 1], students[index + 2])
    else:
        print("error")

for index in range(0, numof_s, 4):
    if index + 1 < numof_s and index + 2 < numof_s and index + 4 < numof_s:
        print(students[index], students[index + 1], students[index + 2], students[index + 3])
    else:
        print("error")