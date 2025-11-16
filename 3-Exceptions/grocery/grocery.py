groceries = {}
while True:
    try:
        item = input().upper()
        if item in groceries:
            groceries[item] += 1
            # print(item, groceries[item])
        else:
            groceries[item] = 1
            # print(item, groceries[item])
    except EOFError:
        # the line below was the problem, it returned a list of keys once sorted
        grocers = sorted(groceries)
        for i in grocers:
            print(groceries[i], i)
