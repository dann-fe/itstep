data = [
    "John",
    "Peter",
    "Lev",
    "Leonard",
    "Patrick"
]

def searcher(letter, characters):
    for i in data:
        if i[0] == letter and len(i) == characters:
            return i
        
        return None

print(searcher("J", 18))