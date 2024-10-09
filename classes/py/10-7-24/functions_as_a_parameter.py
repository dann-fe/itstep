grades = {
    1: 'Výborně',
    2: 'Chvalitebně',
    3: 'Dobře',
    4: 'Dostatečně',
    5: 'Nedostatečně',
    6: 'Katastrofa',
}

def cook():
    print("im cooking")

def get_text_grade(grade: int, callback):
    callback()
    return grades[grade]

print(get_text_grade(3, cook))