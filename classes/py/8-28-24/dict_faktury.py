import os, csv

data = {
    "CENDIS, s.p.": 26999.13,
}

with open ("classes/py/8-19-24-cycles/faktury_md_2024.csv", encoding="utf-8") as file:
    file.readline()
    reader = csv.reader(file)

    for line in reader:
        print(line[3], line[5])

        if line[5] not in data:
            data[line[3]] = float(line[5])
        else:
            data[line[3]] += float(line[5])

data_list = list(data.items())
data_list.sort(key=lambda x: x[1])
print(data_list)    