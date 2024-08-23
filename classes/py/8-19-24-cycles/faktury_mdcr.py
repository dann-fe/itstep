import csv

with open ('classes/py/8-19-24/faktury_md_2024.csv', encoding="utf-8") as file:
    reader = csv.reader(file)
    max_cost = 0
    for line in reader:
        costs = float(line[5])
        company = line[3] + "-" + line[4]
        if costs > max_cost:
            max_cost = costs
            max_company = company

        print(f"{costs} for {company}")
    print(f'the biggest amount is {max_cost} for {max_company}')
