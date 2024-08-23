def do_the_shopping (who: str, store: str, groceries: list):
    print(who, "will do the shopping in", store, "he/she is going to buy")
    print("SHOPPING LIST:")
    for list in groceries:
        print(list)


do_the_shopping("mom", "lidl", ["apples", "2 bananas", "a yogurt"])
    
