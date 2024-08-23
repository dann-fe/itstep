
data = [325, 234, 102, 583, 20, 533, 205, 100, 28, 73]





def graph(data = list, filename = str, color = str):
    with open(filename, mode="w", encoding="utf-8") as file:
       for value in data:
           div = f'<div style="width: {value}px; background-color: {color}; height: 50px; margin-bottom: 5px;"></div>'
           file.write(div)

graph(data, "C:/Users/adamk/Desktop/programovani/step_fullstack/classes/py/8-14-24/graph.html", "green")