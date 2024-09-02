text = "odsfhpn asdufpaweurvtnpowerunpaeorvunapwoerncporcwpeyrcnwierncwaieomhwpocfpohfoasdfhisdfdsifcndosiafycbdcscfdgsoif"
data = {}

for letter in text:
    if letter in data:
        data[letter] += 1
    else:
        data[letter] = 1
print(data)