a = [1, 2, 3]
b = {
    "x": a,
    "y": a
}

print(id(a))
print(id(b["x"]))
print(id(b["y"]))